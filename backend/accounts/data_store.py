from backend.types import ServiceType

class DataStore(ServiceType):
  async def store_account(self, id, email_address, password):
    raise NotImplementedError()

  async def load_account(self, account_id):
    raise NotImplementedError()
