class Server:
  def __init__(self, accounts_client):
    self._accounts_client = accounts_client

  async def acct_handler(self, username):
    pass
