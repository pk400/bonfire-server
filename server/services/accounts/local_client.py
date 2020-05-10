from services.accounts.client import Client
from services.accounts.session import Session
from exceptions import BadCredentialsException


class LocalClient(Client):
  def __init__(self, server):
    self._server = server
    self._session = Session()
    self._email_address = None
    self._password = None
    self._is_logged_in = False

  async def create_account(self, email_address, password):
    return await self._server.create_account(self._session, email_address,
      password)

  def set_credentials(self, email_address, password):
    self._email_address = email_address
    self._password = password

  async def open(self):
    if not self._email_address or not self._password:
      raise BadCredentialsException('Invalid credentials.')
    if not self._is_logged_in:
      self._session.set_credentials(self._email_address, self._password)
      self._is_logged_in = True

  async def close(self):
    if self._is_logged_in:
      self._is_logged_in = False
      self._session.reset_credentials()
