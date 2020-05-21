import uvicorn

from controllers.application_controller import ApplicationController
from lib.accounts.local_data_store import LocalDataStore
from lib.accounts.server import Server
from lib.jwt.jwt import JWT
from lib.password_hasher.bcrypt_password_hasher import BcryptPasswordHasher


def main():
  server = Server(LocalDataStore(), BcryptPasswordHasher())
  server.open()
  jwt = JWT('x')
  application_controller = ApplicationController(server, jwt)
  uvicorn.run(application_controller.asgi_app)


if __name__ == '__main__':
  main()
