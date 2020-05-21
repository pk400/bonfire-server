import unittest

from library import exceptions
from library.accounts.local_data_store import LocalDataStore
from library.accounts.server import Server
from library.accounts.session import Session
from library.password_hasher.test_password_hasher import TestPasswordHasher
from library.utils import run_in_loop


class LoginTester(unittest.TestCase):
  def setUp(self):
    self.data_store = LocalDataStore()
    self.server = Server(self.data_store, TestPasswordHasher())
    self.server.open()

  def tearDown(self):
    self.server.close()

  def test_success(self):
    account_id = run_in_loop(self.server.create_account('a', 'b'))
    session = Session()
    run_in_loop(self.server.login(session, 'a', 'b'))
    self.assertTrue(session.is_modified)
    self.assertEqual(session.id, account_id)

  def test_bad_credentials(self):
    account_id = run_in_loop(self.server.create_account('a', 'b'))
    session = Session()
    run_in_loop(self.server.login(session, 'a', 'b'))
    self.assertTrue(session.is_modified)
    self.assertEqual(session.id, account_id)
    with self.assertRaises(exceptions.SessionLoggedInException):
      run_in_loop(self.server.login(session, 'a', 'b'))


if __name__ == '__main__':
  unittest.main()
