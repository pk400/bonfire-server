from starlette import status
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Route
from starlette.responses import JSONResponse, Response

from bonfire.library.accounts.server import Server
from bonfire.library.middleware.session_middleware import SessionMiddleware
from bonfire.library.exceptions import BonfireException
from bonfire.models.actor import Actor


class AccountsController:
  def __init__(self, server, jwt):
    self._server = server
    self._jwt = jwt
    routes = [
      Route('/register', self.register, name='register', methods=['POST']),
      Route('/login', self.login, name='login', methods=['POST']),
      Route('/logout', self.logout, name='logout', methods=['POST']),
      Route('/load_account', self.load_account, name='load_account',
        methods=['POST']),
      Route('/actor', self.actor, name='actor', methods=['GET'])
    ]
    middleware = [
      Middleware(SessionMiddleware, cookie_name='session_id', jwt=jwt)
    ]
    exception_handlers = {
      BonfireException: self.bonfire_exception_handler
    }
    self._asgi_app = Starlette(routes=routes, middleware=middleware,
      exception_handlers=exception_handlers)

  @property
  def asgi_app(self):
    return self._asgi_app

  async def register(self, request):
    params = await request.form()
    account_id = await self._server.create_account(request.session,
      params['email_address'], params['username'], params['password'])
    return JSONResponse({'account_id': account_id},
      status_code=status.HTTP_201_CREATED)

  async def login(self, request):
    params = await request.form()
    await self._server.login(request.session, params['email_address'],
      params['password'])
    return Response(status_code=status.HTTP_200_OK)

  async def logout(self, request):
    await self._server.logout(request.session)
    return Response(status_code=status.HTTP_200_OK)

  async def load_account(self, request):
    params = await request.json()
    if 'id' in params:
      account = await self._server.load_account_by_id(request.session,
        params['id'])
    elif 'email_address' in params:
      account = await self._server.load_account_by_username(
        request.session, params['email_address'])
    else:
      return Response(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(account.to_json(), status_code=status.HTTP_200_OK)

  async def bonfire_exception_handler(self, request, exc):
    if exc.code == Server.LOGIN_FAILED:
      return Response(status_code=status.HTTP_401_UNAUTHORIZED)

  async def actor(self, request):


    return JSONResponse({
      "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1"
      ],

      "id": "https://983c4a97.ngrok.io/api/accounts/actor",
      "type": "Person",
      "preferredUsername": "joel",
      "inbox": "https://my-example.com/inbox",
    })
