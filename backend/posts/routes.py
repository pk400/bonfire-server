from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response

app = Starlette()

@app.exception_handler(ValueError)
async def on_value_error(request, exc):
  return Response(status_code=400)

@app.route('/posts', methods=['GET'])
async def on_load_post_filtered(request):
  params = request.query_params
  post_filter = {
    'range': (int(params['from']), int(params['to'])),
    'limit': int(params['limit'])
  }
  posts = await app.state.api.search_posts(post_filter)
  return JSONResponse([post.to_json() for post in posts])

@app.route('/posts/{post_id}', methods=['GET'])
async def on_load_post(request):
  post = await app.state.api.load_post(int(request.path_params['post_id']))
  return JSONResponse(post.to_json())

@app.route('/posts', methods=['POST'])
async def on_create(request):
  params = await request.form()
  await app.state.api.create_post(params['title'], params['image_file'],
    params['content'])
  return Response(status_code=204)

@app.route('/posts', methods=['PUT'])
async def on_update(request):
  pass

@app.route('/posts', methods=['DELETE'])
async def on_remove(request):
  pass

@app.route('/posts', methods=['PATCH'])
async def on_partial_update(request):
  pass
