from backend.accounts import Server
from backend.http_servers.starlette import StarletteHttpServer

import uvicorn

if __name__ == '__main__':
  uvicorn.run(StarletteHttpServer)
