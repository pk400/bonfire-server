from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
import uvicorn

from . import Account, LocalDataBase

def BonfireApplication(database):
  app = Starlette()

  @app.route('/register', methods=['POST'])
  async def register(request):
    params = await request.json()
    account = Account(params['username'], params['password'])
    database.store_account(account)
    return PlainTextResponse(account.username)

  @app.route('/login', methods=['POST'])
  async def login(request):
    params = await request.json()
    account = database.load_account(params['username'])
    response = PlainTextResponse('Could not log in.'.encode('utf-8'))
    if account.password == params['password']:
      response.set_cookie('account', account.username)
      response.body = 'Logged in!'.encode('utf-8')
    return response

  @app.route('/.well-known/webfinger', methods=['GET'])
  async def webfinger(request):
    request_user = request.query_params['resource'].split(':')[1].split('@')[0]
    account = database.load_account(request_user)
    if not account:
      return PlainTextResponse('Could not find user.')
    return JSONResponse(account.webfinger)
  
  @app.route('/users/{username}')
  async def users(request):
    username = request.path_params['username']
    account = database.load_account(username)
    if not account:
      return PlainTextResponse('Could not find user.')
    return JSONResponse(account.actor)

  return app
