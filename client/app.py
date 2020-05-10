from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')


async def on_register(request):
  return templates.TemplateResponse('register.jinja', {'request': request})


async def on_login(request):
  return templates.TemplateResponse('login.jinja', {'request': request})


routes = [
  Mount('/static', StaticFiles(directory='static')),
  Route('/register', on_register),
  Route('/login', on_login)
]


app = Starlette(routes=routes)
