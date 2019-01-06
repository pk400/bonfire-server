import unittest

from starlette.applications import Starlette
from starlette.testclient import TestClient

from server import asgi

class ServerTests(unittest.TestCase):
  def setUp(self):
    self.client = TestClient(asgi.app)
  
  def ensure_status_code(self, expected, received):
    self.assertEqual(expected, received)
    
  def test_create_account(self):
    response = self.client.get('/create_account')
    self.ensure_status_code(200, response.status_code)

  def test_inbox_get(self):
    response = self.client.get('/inbox')
    self.ensure_status_code(200, response.status_code)

  def test_inbox_post(self):
    response = self.client.post('/inbox')
    self.ensure_status_code(200, response.status_code)
  
if __name__ == '__main__':
  unittest.main()
