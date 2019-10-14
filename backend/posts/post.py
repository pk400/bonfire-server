class Post:
  def __init__(self, post_id, title, image_id, content):
    self._post_id = post_id
    self._title = title
    self._image_id = image_id
    self._content = content

  @property
  def post_id(self):
    return self._post_id

  @property
  def title(self):
    return self._title

  @property
  def image_id(self):
    return self._image_id

  @property
  def content(self):
    return self._content

  def to_json(self):
    return self.__dict__

class EmptyPost(Post):
  def __init__(self):
    super().__init__(None, None, None, None)
