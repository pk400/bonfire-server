class PostsAPI:
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

  async def search_posts(self, filter):
    posts = await self._data_store.search_posts(filter)
    return posts

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
