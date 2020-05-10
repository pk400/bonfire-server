import argparse
import os

import uvicorn
import yaml

from applications.accounts_service.http_server import HttpServer
from services.accounts.server import Server
from services.accounts.local_data_store import LocalDataStore
from library.password_hasher.bcrypt_password_hasher import \
  BcryptPasswordHasher


def main():
  arg_parser = argparse.ArgumentParser()
  arg_parser.add_argument('-c', '--config',
    help='Application configuration file.', default='config.yml')
  args = arg_parser.parse_args()
  configs = yaml.safe_load(open(args.config))
  data_store = LocalDataStore()
  password_hasher = BcryptPasswordHasher()
  server = Server(data_store, password_hasher)
  server.open()
  http_server = HttpServer(server)
  if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
  else:
    port = int(configs['port'])
  uvicorn.run(http_server.app, host=configs['host'], port=port)


if __name__ == '__main__':
  main()
