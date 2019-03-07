from account import Account
from utils import require_open

class Api:
  def __init__(self, db):
    self._db = db
    self._is_open = False
  
  @require_open
  async def register(self, **params):
    try:
      account = Account(params['username'], params['password'],
        params['email_address'])
      self._db.register(account)
      return True
    except Exception:
      return False

  @require_open
  async def login(self, **params):
    pass
  
  def open(self):
    self._is_open = True
  
  def close(self):
    self._is_open = False
