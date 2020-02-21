from backend.accounts import Account, Session
from backend.exceptions import BadCredentialsException
from backend.types import SequenceGenerator, ServiceType
from backend.utils import require_open

class Server(ServiceType):
  LOGIN_FAILED = 0

  def __init__(self, data_store):
    self._data_store = data_store
    self._account_id_generator = SequenceGenerator(0)

  def startup(self):
    pass

  def shutdown(self):
    pass

  @require_open
  async def create_account(self, session, email_address, password):
    # TODO: Validate session
    # TODO: Hash password
    hashed_password = None
    await self._data_store.store_account(self._account_id_generator.generate(),
      email_address, hashed_password)

  @require_open
  async def login(self, session, email_address, password):
    # TODO: Validate session
    account_id = await self._data_store.load_account_id_by_email(email_address)
    if account_id == -1:
      raise BadCredentialsException('Login failed.', Server.LOGIN_FAILED)
    hashed_password = await self._data_store.load_password(account_id)
    # TODO: Compare unhashed password

  @require_open
  async def logout(self, session):
    session.reset_credentials()
