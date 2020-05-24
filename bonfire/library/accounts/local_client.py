from bonfire.library.accounts.client import Client
from bonfire.library.accounts.session import Session
from bonfire.library.utils import run_in_loop


class LocalClient(Client):
  def __init__(self, server):
    self._server = server
    self._session = Session()
    self._username = None
    self._password = None
    self._is_open = False

  async def create_account(self, email_address, username, password):
    return await self._server.create_account(self._session, email_address,
      username, password)

  async def load_account_by_id(self, account_id):
    return await self._server.load_account_by_id(self._session, account_id)

  async def load_account_by_email_address(self, email_address):
    return await self._server.load_account_by_email_address(self._session,
      email_address)

  def set_credentials(self, username, password):
    self._username = username
    self._password = password

  def open(self):
    if not self._is_open:
      run_in_loop(self._server.login(self._session, self._username,
        self._password))
      self._is_open = True

  async def close(self):
    if self._is_open:
      self._is_open = False
