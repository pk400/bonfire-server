from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
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

templates = Jinja2Templates(directory='bonfire/views')


async def login(request):
  return templates.TemplateResponse('login.jinja', {
    'request': request,
  })


async def register(request):
  return templates.TemplateResponse('register.jinja', {
    'request': request,
  })


if __name__ == '__main__':
  server = Server(LocalDataStore(), BcryptPasswordHasher())
  server.open()
  accounts_controller = AccountsController(server, JWT('x'))
  accounts_client = LocalClient(server)
  run_in_loop(accounts_client.create_account('a', 'b', 'c'))
  accounts_client.set_credentials('a', 'c')
  accounts_client.open()
  webfinger_controller = WebFingerController(accounts_client)
  routes = [
    Mount('/public', StaticFiles(directory='public'), name='static'),
    Mount('/.well-known', webfinger_controller.asgi_app),
    Route('/login', login, name='login'),
    Route('/register', register, name='register'),
    Mount('/api', name='api', routes=[
      Mount('/accounts', accounts_controller.asgi_app, name='accounts')
    ])
  ]
  app = Starlette(routes=routes)
  uvicorn.run(app)
