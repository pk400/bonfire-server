import uvicorn

from api import Api
from asgi import AsgiApplication
from local_database import LocalDataBase

if __name__ == '__main__':
  app = AsgiApplication(Api(LocalDataBase()))
  config = {
    'host': '0.0.0.0',
    'port': 8001
  }
  uvicorn.run(app, **config)
