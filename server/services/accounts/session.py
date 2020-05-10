from library.serializer import Serializer


class Session:
  def __init__(self):
    self._id = None

  @property
  def id(self):
    return self._id

  def set_credentials(self, id):
    self._id = id

  def reset_credentials(self):
    self._id = None

  def to_json(self):
    return Serializer.dict_to_json({
      'id': self._id
    })

  def from_json(self, mapping):
    session = Session()
    session.set_credentials(Serializer.from_json(mapping['id'], int))
    return session

  def __eq__(self, other):
    return self._id == other.id


Session.EMPTY = Session()
