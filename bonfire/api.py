import asyncio

from bonfire.utils import require_open

class Api:
  def __init__(self, dsn):
    self._dsn = dsn
    self._connection_pool = None
    self._is_open = False
  
  @require_open
  async def register(self, username, password):
    await self._execute_query('''
      INSERT INTO accounts (username, password)
      VALUES (%s, %s)
      ''', (username, password))
    return True

  @require_open
  async def login(self, **params):
    pass

  @require_open
  async def find_account(self, username):
    result = await self._execute_query('''
      SELECT username, password
      FROM accounts
      WHERE username=%s
      ''', (username,))
    return result
  
  def open(self):
    loop = asyncio.get_event_loop()
    loop.create_task(self._open_db())
    self._is_open = True
  
  def close(self):
    self._is_open = False

  async def _open_db(self):
    self._connection_pool = await asyncpg.create_pool(self._dsn)
    await self._execute_query('''
      CREATE TABLE IF NOT EXISTS accounts (
        id SERIAL,
        username TEXT,
        password TEXT);''')
  
  async def _execute_query(self, query, params=None):
    if params is None:
      params = {}
    async with self._connection_pool.acquire() as con:
      return con.execute(query, params)

