from starlette.testclient import TestClient
import unittest

from bonfire.controllers.webfinger_controller import WebFingerController
from bonfire.library import accounts
from bonfire.library.utils import run_in_loop
from tests.test_password_hasher import TestPasswordHasher


class WebFingerTester(unittest.TestCase):
  def test_success(self):
    server = accounts.Server(accounts.LocalDataStore(), TestPasswordHasher())
    server.open()
    accounts_client = accounts.LocalClient(server)
    run_in_loop(accounts_client.create_account('a', 'b', 'c'))
    accounts_client.set_credentials('a', 'c')
    accounts_client.open()
    controller = WebFingerController(accounts_client)
    with TestClient(controller.asgi_app) as client:
      response = client.get('/webfinger', params={
        'resource': 'acct:a'
      })
    self.assertDictEqual(response.json(), {
      'subject': 'a',
      'aliases': [],
      'properties': {},
      'links': []
    })


if __name__ == '__main__':
  unittest.main()
