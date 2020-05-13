from applications.accounts_service.http_server import HttpServer
from services.accounts.server import Server
from services.accounts.local_data_store import LocalDataStore
from library.password_hasher.bcrypt_password_hasher import BcryptPasswordHasher


def main():
  data_store = LocalDataStore()
  password_hasher = BcryptPasswordHasher()
  server = Server(data_store, password_hasher)
  server.open()
  http_server = HttpServer(server)
  return http_server.app

app = main()

if __name__ == '__main__':
  main()
