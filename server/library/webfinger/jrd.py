from library.serializer import Serializer


class JRD:
  def __init__(self, subject, alias, properties, links):
    self._subject = subject
    self._alias = alias
    self._properties = properties
    self._links = links

  @property
  def subject(self):
    return self._subject

  @property
  def alias(self):
    return self._alias

  @property
  def properties(self):
    return self._properties

  @property
  def links(self):
    return self._links

  def to_json(self):
    return Serializer.dict_to_json({
      'subject': self._subject,
      'alias': self._alias,
      'properties': self._properties,
      'links': self._links
    })
