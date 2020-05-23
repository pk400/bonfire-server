import uvicorn

from controllers.application_controller import ApplicationController
from bonfire.library.accounts.local_data_store import LocalDataStore
from bonfire.library.accounts.server import Server
from bonfire.library.jwt.jwt import JWT
from bonfire.library.password_hasher.bcrypt_password_hasher import BcryptPasswordHasher


def main():
  server = Server(LocalDataStore(), BcryptPasswordHasher())
  server.open()
  jwt = JWT('x')
  application_controller = ApplicationController(server, jwt)
  uvicorn.run(application_controller.asgi_app)


if __name__ == '__main__':
  main()
