from starlette import status
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Route
from starlette.responses import JSONResponse, Response

from bonfire.library.middleware.session_middleware import SessionMiddleware


class AccountsController:
  def __init__(self, server, jwt):
    self._server = server
    self._jwt = jwt
    routes = [
      Route('/register', self.register, methods=['POST']),
      Route('/login', self.login, methods=['POST']),
      Route('/logout', self.logout, methods=['POST']),
      Route('/load_account', self.load_account, methods=['POST'])
    ]
    middleware = [
      Middleware(SessionMiddleware, cookie_name='session_id', jwt=jwt)
    ]
    self._asgi_app = Starlette(routes=routes, middleware=middleware)

  @property
  def asgi_app(self):
    return self._asgi_app

  async def register(self, request):
    params = await request.json()
    account_id = await self._server.create_account(request.session,
      params['email_address'], params['username'], params['password'])
    return JSONResponse({'account_id': account_id},
      status_code=status.HTTP_201_CREATED)

  async def login(self, request):
    params = await request.json()
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
