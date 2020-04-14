import collections
import unittest

import bcrypt

from server import exceptions
from server.accounts.account import Account
from server.accounts.account_entry import AccountEntry
from server.accounts.local_data_store import LocalDataStore
from server.accounts.server import Server
from server.accounts.session import Session
from server.utils import run_in_loop

MockAccountData = \
  collections.namedtuple('MockAccountData', ['id', 'email_address', 'password'])

class LoginTester(unittest.TestCase):
  def setUp(self):
    self.data_store = LocalDataStore()
    self.server = Server(self.data_store)
    self.server.open()

  def tearDown(self):
    self.server.close()

  def test_success(self):
    data = MockAccountData(99, 'a', 'b')
    hashed = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
    self.data_store._accounts[data.id] = \
      AccountEntry(Account(data.id, data.email_address), hashed)
    self.data_store._email_address_to_id[data.email_address] = data.id
    run_in_loop(self.server.login(Session(), data.email_address, data.password))

  def test_bad_credentials(self):
    data = MockAccountData(99, 'a', 'b')
    hashed = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
    self.data_store._accounts[data.id] = \
      AccountEntry(Account(data.id, data.email_address), hashed)
    self.data_store._email_address_to_id[data.email_address] = data.id
    with self.assertRaises(exceptions.BadCredentialsException) as error:
      run_in_loop(self.server.login(Session(), data.email_address, 'bad'))
    self.assertEqual(error.exception.code, Server.LOGIN_FAILED)

  def test_already_logged_in(self):
    data = MockAccountData(99, 'a', 'b')
    hashed = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
    self.data_store._accounts[data.id] = \
      AccountEntry(Account(data.id, data.email_address), hashed)
    session = Session()
    session.set_credentials(data.id)
    with self.assertRaises(exceptions.SessionLoggedInException) as error:
      run_in_loop(self.server.login(session, data.email_address, data.password))
    self.assertEqual(error.exception.code, Server.SESSION_LOGGED_IN)

if __name__ == '__main__':
  unittest.main()
