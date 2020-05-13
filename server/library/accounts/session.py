from library.serializer import Serializer


def is_mutable(inner_func):
  def wrapper(self, *args, **kwargs):
    if not self._is_modified:
      self._is_modified = True
    return inner_func(self, *args, **kwargs)
  return wrapper


class Session:
  def __init__(self, id=None):
    self._id = id
    self._is_modified = False

  @property
  def id(self):
    return self._id

  @property
  def is_modified(self):
    return self._is_modified

  @is_mutable
  def set_credentials(self, id):
    self._id = id

  @is_mutable
  def reset_credentials(self):
    self._id = None

  def to_json(self):
    return Serializer.dict_to_json({
      'id': self._id
    })

  @staticmethod
  def from_json(mapping):
    session = Session()
    session.set_credentials(Serializer.from_json(mapping['id'], int))
    return session

  def __eq__(self, other):
    return self._id == other.id


Session.EMPTY = Session()
