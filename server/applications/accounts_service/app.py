from library.accounts.http_server import HttpServer
from library.accounts.local_data_store import LocalDataStore
from library.accounts.server import Server
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
