from starlette import status
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from middleware.session_middleware import SessionMiddleware


class HttpServer:
  def __init__(self, server):
    self._server = server
    self._app = Starlette(routes=[
      Route('/create_account', self._on_create_account, methods=['POST'],
        name='create_account'),
      Route('/login', self._on_login, methods=['POST'], name='login'),
      Route('/logout', self._on_logout, methods=['POST'], name='logout')
    ], middleware=[Middleware(SessionMiddleware, cookie_name='jwt')])

  @property
  def app(self):
    return self._app

  async def _on_create_account(self, request):
    params = await request.json()
    account_id = await self._server.create_account(request.state.session,
      params['email_address'], params['password'])
    return JSONResponse({'account_id': account_id},
      status_code=status.HTTP_201_CREATED)

  async def _on_login(self, request):
    params = await request.json()
    await self._server.login(request.state.session, params['email_address'],
      params['password'])
    return Response(status_code=status.HTTP_200_OK)

  async def _on_logout(self, request):
    await self._server.logout(request.state.session)
    return Response(status_code=status.HTTP_200_OK)
