class JRD:
  def __init__(self, subject, aliases=[], properties={}, links=[]):
    self._subject = subject
    self._aliases = aliases
    self._properties = properties
    self._links = links

  def to_json(self):
    return {
      'subject': self._subject,
      'aliases': self._aliases,
      'properties': self._properties,
      'links': self._links
    }
