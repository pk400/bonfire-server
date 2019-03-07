from starlette.applications import Starlette
from starlette.responses import JSONResponse
from webfinger import WebfingerAsgi

def AsgiApplication(api):
  app = Starlette()
  app.mount('/.well-known/webfinger', WebfingerAsgi())

  @app.route('/register', methods=['POST'])
  async def on_register(request):
    params = await request.json()
    return JSONResponse(api.register(**params))

  @app.route('/login', methods=['POST'])
  async def on_login(request):
    params = await request.json()
    return JSONResponse(api.register(**params))

  return app
