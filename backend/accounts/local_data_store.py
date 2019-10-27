from accounts.account import Account
from accounts.data_store import DataStore

class LocalDataStore(DataStore):
  def __init__(self):
    self._accounts = {}

  def open(self):
    self._is_open = True

  def close(self):
    self._is_open = False

  async def store_account(self, account):
    self._accounts[account.account_id] = account

  async def load_account_from_id(self, account_id):
    return self._accounts.get(account_id, Account.NONE)
