from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()

@app.route('/.well-known/webfinger')
async def on_webfinger(request):
  params = await request.query_params()
  scheme, resource = params.split(':')
  # TODO: Retrieve user from database
  return JSONResponse()
