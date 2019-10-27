from uuid import uuid4

from accounts.account import Account

class Api:
  def __init__(self, data_store):
    self._data_store = data_store

  async def create_account(self, username, email_address, password):
    account = Account(self._generate_account_id(), username, email_address,
      password)
    await self._data_store.store_account(account)

  async def load_account_from_id(self, account_id):
    account = await self._data_store.load_account_from_id(account_id)

  def _generate_account_id(self):
    return uuid4()
