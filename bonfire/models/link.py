from bonfire.library.serializer import Serializer


class Link:
  def __init__(self, rel, __type=None, href=None, titles={}):
    self._rel = rel
    self._type = __type
    self._href = href
    self._titles = titles

  def to_json(self):
    json = {
      'rel': self._rel
    }
    if self._type is not None:
      json['type'] = self._type
    if self._href is not None:
      json['href'] = self._href
    if self._titles:
      json['titles'] = self._titles
    return Serializer.to_json(json)
