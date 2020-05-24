class Link:
  def __init__(self, rel, __type=None, href=None, titles={}):
    self._rel = rel
    self._type = __type
    self._href = href
    self._titles = titles
