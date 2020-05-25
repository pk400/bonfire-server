from starlette.applications import Starlette
from starlette.routing import Mount
import uvicorn

from bonfire.controllers.accounts_controller import AccountsController
from bonfire.controllers.webfinger_controller import WebFingerController
from bonfire.library.accounts.local_client import LocalClient
from bonfire.library.accounts.local_data_store import LocalDataStore
from bonfire.library.accounts.server import Server
from bonfire.library.jwt.jwt import JWT
from bonfire.library.password_hasher.bcrypt_password_hasher import \
  BcryptPasswordHasher
from bonfire.library.utils import run_in_loop


def main():
  server = Server(LocalDataStore(), BcryptPasswordHasher())
  server.open()
  jwt = JWT('x')
  accounts_controller = AccountsController(server, jwt)
  accounts_client = LocalClient(server)
  run_in_loop(accounts_client.create_account('a', 'b', 'c'))
  accounts_client.set_credentials('a', 'c')
  accounts_client.open()
  webfinger_controller = WebFingerController(accounts_client)
  routes = [
    Mount('/api/accounts', accounts_controller.asgi_app),
    Mount('/.well-known', webfinger_controller.asgi_app)
  ]
  app = Starlette(routes=routes)
  uvicorn.run(app)


if __name__ == '__main__':
  main()
