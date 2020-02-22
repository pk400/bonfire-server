import bcrypt

from backend.accounts.account import Account
from backend.accounts.session import Session
from backend.exceptions import BadCredentialsException
from backend.types import SequenceGenerator, ServiceType
from backend.utils import require_open

class Server(ServiceType):
  LOGIN_FAILED = 0

  def __init__(self, data_store):
    self._data_store = data_store
    self._account_id_generator = SequenceGenerator(-1)

  def startup(self):
    self._data_store.open()

  def shutdown(self):
    self._data_store.close()

  @require_open
  async def create_account(self, email_address, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    account_id = self._account_id_generator.generate()
    await self._data_store.store_account(account_id, email_address,
      hashed_password)
    return account_id

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
