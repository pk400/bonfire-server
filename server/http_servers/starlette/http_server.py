from starlette import status
from starlette.applications import Starlette
from starlette.responses import Response

from server.accounts import Server, LocalDataStore

StarletteHttpServer = Starlette()

@StarletteHttpServer.route('/create_account')
async def on_create_account(request):
  params = await request.json()
  await routes.on_create_account(request.state.session, params[''])
  return Response(status_code=status.HTTP_201_CREATED)

@StarletteHttpServer.route('/login')
async def on_login(request):
  return Response(status_code=status.HTTP_200_OK)

@StarletteHttpServer.route('/logout')
async def on_logout(request):
  return Response(status_code=status.HTTP_200_OK)
