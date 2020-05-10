from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import yaml


templates = Jinja2Templates(directory='templates')
config = yaml.safe_load(open('config.yml'))


async def on_register(request):
  return templates.TemplateResponse('register.jinja', {
    'request': request,
    'register_url': config['accounts_url'] + '/create_account'
  })


async def on_login(request):
  return templates.TemplateResponse('login.jinja', {
    'request': request
  })


routes = [
  Mount('/static', StaticFiles(directory='static'), name='static'),
  Route('/register', on_register, name='register'),
  Route('/login', on_login, name='login')
]


app = Starlette(routes=routes)
