import abc

from interfaces.data_store import DataStore

class DataStore(DataStore):
  @abc.abstractmethod
  async def store_account(self, account):
    pass

  @abc.abstractmethod
  async def load_account_from_id(self, account_id):
    pass

  @abc.abstractmethod
  async def remove_account(self, account_id):
    pass
