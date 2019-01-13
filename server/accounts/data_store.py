from abc import ABC

class DataStore(ABC):
  def store_account(self, account):
    '''Store a user account into the datastore.
    
    Args:
      account (Account): Account object to be stored.
    '''
    raise NotImplementedError()
  
  def load_account(self, id):
    '''Load a user account from the datastore.

    Args:
      id (Account.id): The id of the account to be retrieved.
    '''
    raise NotImplementedError()
