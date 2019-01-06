from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()

@app.route('/create_account')
def create_account(request):
  return JSONResponse('create_account')

@app.route('/inbox', methods=['GET', 'POST'])
def inbox(request):
  return JSONResponse('inbox')
