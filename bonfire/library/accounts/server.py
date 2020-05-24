from bonfire.library import exceptions
from bonfire.library.accounts.session import Session
from bonfire.library.generators.sequence_generator import SequenceGenerator
from bonfire.library.types.service_type import ServiceType
from bonfire.library.utils import require_open


class Server(ServiceType):
  LOGIN_FAILED = 0
  SESSION_LOGGED_IN = 1

  def __init__(self, data_store, password_hasher):
    super().__init__()
    self._data_store = data_store
    self._password_hasher = password_hasher
    self._account_id_generator = SequenceGenerator(-1)

  def startup(self):
    self._data_store.open()

  def shutdown(self):
    self._data_store.close()

  @require_open
  async def create_account(self, session, email_address, username, password):
    account_id = self._account_id_generator.generate()
    await self._data_store.store_account(account_id, email_address, username,
      self._password_hasher.hash_password(password))
    return account_id

  @require_open
  async def login(self, session, email_address, password):
    if session != Session.EMPTY:
      raise exceptions.SessionLoggedInException(
        'Session is already logged in.', Server.SESSION_LOGGED_IN)
    account_id = \
      await self._data_store.load_account_id_by_email_address(email_address)
    hashed_password = await self._data_store.load_password(account_id)
    is_password_validated = self._password_hasher.check_password(password,
      hashed_password)
    if not is_password_validated:
      raise exceptions.BadCredentialsException('Login failed.',
        Server.LOGIN_FAILED)
    session.set_credentials(account_id)

  @require_open
  async def logout(self, session):
    session.reset_credentials()

  @require_open
  async def load_account_by_id(self, session, account_id):
    account = await self._data_store.load_account_by_id(account_id)
    return account

  @require_open
  async def load_account_by_email(self, session, username):
    account = await self._data_store.load_account_by_email(username)
    return account
