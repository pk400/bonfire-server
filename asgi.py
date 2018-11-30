from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()

@app.route('/')
def index(request):
  return JSONResponse({'message': 'hello world'})
