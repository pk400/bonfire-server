from services.accounts import Account
from services.accounts.account_entry import AccountEntry
from services.accounts.data_store import DataStore
from utils import require_open


class LocalDataStore(DataStore):
  def __init__(self):
    super().__init__()
    self._accounts = {}
    self._email_address_to_id = {}

  def startup(self):
    pass

  def shutdown(self):
    pass

  @require_open
  async def load_account_id_by_email(self, email_address):
    return self._email_address_to_id.get(email_address,
      AccountEntry.NONE.account.id)

  @require_open
  async def store_account(self, account_id, email_address, hashed_password):
    self._accounts[account_id] = AccountEntry(
      Account(account_id, email_address), hashed_password)
    self._email_address_to_id[email_address] = account_id

  @require_open
  async def load_account(self, account_id):
    account_entry = self._accounts.get(account_id, AccountEntry.NONE)
    return account_entry.account

  @require_open
  async def load_password(self, account_id):
    account_entry = self._accounts.get(account_id, AccountEntry.NONE)
    return account_entry.password
