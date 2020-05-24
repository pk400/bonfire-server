from starlette.applications import Starlette
from starlette.routing import Mount
import uvicorn

from bonfire.controllers.accounts_controller import AccountsController
from bonfire.library.accounts.local_data_store import LocalDataStore
from bonfire.library.accounts.server import Server
from bonfire.library.jwt.jwt import JWT
from bonfire.library.password_hasher.bcrypt_password_hasher import \
  BcryptPasswordHasher


def main():
  server = Server(LocalDataStore(), BcryptPasswordHasher())
  server.open()
  jwt = JWT('x')
  accounts_controller = AccountsController(server, jwt)
  routes = [
    Mount('/api/accounts', accounts_controller.asgi_app)
  ]
  app = Starlette(routes=routes)
  uvicorn.run(app)


if __name__ == '__main__':
  main()
