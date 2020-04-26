from server import exceptions
from server.services.accounts.session import Session
from server.types import SequenceGenerator, ServiceType
from server.utils import require_open


class Server(ServiceType):
  LOGIN_FAILED = 0
  SESSION_LOGGED_IN = 1

  def __init__(self, data_store, password_hasher):
    self._data_store = data_store
    self._password_hasher = password_hasher
    self._account_id_generator = SequenceGenerator(-1)

  def startup(self):
    self._data_store.open()

  def shutdown(self):
    self._data_store.close()

  @require_open
  async def create_account(self, email_address, password):
    account_id = self._account_id_generator.generate()
    await self._data_store.store_account(account_id, email_address,
      self._password_hasher.hash_password(password))
    return account_id

  @require_open
  async def login(self, session, email_address, password):
    login_success = False
    if session != Session.EMPTY:
      raise exceptions.SessionLoggedInException(
        'Session is already logged in.', Server.SESSION_LOGGED_IN)
    account_id = await self._data_store.load_account_id_by_email(email_address)
    hashed_password = await self._data_store.load_password(account_id)
    if self._password_hasher.check_password(password, hashed_password):
      session.set_credentials(account_id)
      login_success = True
    if not login_success:
      raise exceptions.BadCredentialsException('Login failed.',
        Server.LOGIN_FAILED)
    return login_success

  @require_open
  async def logout(self, session):
    session.reset_credentials()
