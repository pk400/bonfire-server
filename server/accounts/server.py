from . import Account

class Server:
  def __init__(self, data_store):
    self._data_store = data_store
  
  def create_account(self, params):
    account = Account(
      0,params['username'], params['password'], params['email_address'])
    self._data_store.store_account(account)
    return account
