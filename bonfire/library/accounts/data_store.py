from bonfire.library.types import ServiceType


class DataStore(ServiceType):
  async def store_account(self, id, username, password):
    raise NotImplementedError()

  async def load_account_by_id(self, account_id):
    raise NotImplementedError()

  async def load_account_id_by_email_address(self, email_address):
    raise NotImplementedError()

  async def load_account_by_email_address(self, email_address):
    raise NotImplementedError()

  async def load_password(self, account_id):
    raise NotImplementedError()
