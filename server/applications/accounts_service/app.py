import os

import uvicorn

from server.applications.accounts_service.http_server import HttpServer
from server.services.accounts.server import Server
from server.services.accounts.local_data_store import LocalDataStore
from server.types.password_hasher.bcrypt_password_hasher import \
  BcryptPasswordHasher
from server.utils import run_in_loop


def main():
  data_store = LocalDataStore()
  password_hasher = BcryptPasswordHasher()
  server = Server(data_store, password_hasher)
  server.open()
  http_server = HttpServer(server)
  port = os.environ['PORT']
  uvicorn.run(http_server.app, host='0.0.0.0', port=port)


if __name__ == '__main__':
  main()
