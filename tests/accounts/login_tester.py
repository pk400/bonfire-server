import unittest
import unittest.mock

from backend.accounts.local_data_store import LocalDataStore
from backend.accounts.server import Server


class HashedPasswordStore:
  def __init__(self):
    self._hashed_passwords = {}
    self._id = 0

  def hashpw(self, password):
    _id = self._id
    self._hash[_id] = password
    self._id += 1
    return _id

  def checkpw(self, _hash):
    print(self._hashed_passwords)
    print(_hash.decode('utf-8'))
    return _hash.decode('utf-8') in self._hashed_passwords

  def gensalt(self):
    pass


@unittest.mock.patch('server.accounts.server.bcrypt', HashedPasswordStore)
class LoginTester(unittest.TestCase):
  def test_success(self):
    data_store = LocalDataStore()
    server = Server(data_store)
    server.open()
    server.close()


if __name__ == '__main__':
  unittest.main()
