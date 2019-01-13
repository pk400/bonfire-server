import unittest

from starlette.testclient import TestClient

from server.accounts import LocalDataStore, Server
from server.applications import AccountsHttpServer

class TestAsgi(unittest.TestCase):
  def setUp(self):
    data_store = LocalDataStore()
    server = Server(data_store)
    self.client = TestClient(AccountsHttpServer(server))

  def test_create_account(self):
    response = self.client.post('/create_account', json={
      'username': 'a',
      'password': 'p',
      'email_address': 'e'
    })
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), 'a')
  
  def test_create_account_invalid_params(self):
    response = self.client.post('/create_account', json={
      'username': 'a'
    })
    self.assertEqual(response.status_code, 400)
