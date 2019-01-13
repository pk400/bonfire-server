from . import DataStore

class LocalDataStore(DataStore):
  def __init__(self):
    self._data_store = {}

  def store_account(self, account):
    self._data_store[account.id] = account

  def load_account(self, id):
    return self._data_store[id]
