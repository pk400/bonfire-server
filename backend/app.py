from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse, FileResponse

from data_store import LocalDataStore
from post import Post

class Server:
  def __init__(self, data_store):
    self._post_id = 0
    self._image_id = 0
    self._data_store = data_store

  async def create_post(self, title, image_file, content):
    image_id = self._generate_image_id()
    post = Post(self._generate_post_id(), title, image_id, content)
    await self._data_store.store_image_file(image_id, image_file)
    await self._data_store.store_post(post)

  async def load_all_posts(self):
    return await self._data_store.load_all_posts()

  async def load_post(self, post_id):
    post = await self._data_store.load_post(post_id)
    return post

  async def load_image(self, image_id):
    return await self._data_store.load_image(image_id)

  def _generate_post_id(self):
    temp = self._post_id
    self._post_id += 1
    return temp

  def _generate_image_id(self):
    temp = self._image_id
    self._image_id += 1
    return temp

app = Starlette()
server = Server(LocalDataStore())

@app.route('/')
async def on_index(request):
  return HTMLResponse(open('index.html').read())

@app.route('/create_post', methods=['POST'])
async def on_create_post(request):
  params = await request.form()
  await server.create_post(params['title'], params['image_file'],
    params['content'])
  return HTMLResponse(open('index.html').read())

@app.route('/load_all_posts', methods=['POST'])
async def on_load_all_posts(request):
  posts = {
    post.post_id: {
      'title': post.title,
      'image_id': post.image_id,
      'content': post.content
    } for post in await server.load_all_posts()}
  return JSONResponse(posts)

@app.route('/load_post', methods=['POST'])
async def on_load_post(request):
  pass

@app.route('/load_image', methods=['POST'])
async def on_load_image(request):
  params = await request.json()
  image = await server.load_image(params['image_id'])
  print(image.file)
  return FileResponse(image.file)
