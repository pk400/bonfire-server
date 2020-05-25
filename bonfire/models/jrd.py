from bonfire.library.serializer import Serializer


class JRD:
  def __init__(self, subject, aliases=[], properties={}, links=[]):
    self._subject = subject
    self._aliases = aliases
    self._properties = properties
    self._links = links

  def to_json(self):
    data = {
      'subject': self._subject,
      'links': self._links
    }
    if len(self._aliases) > 0:
      data['aliases'] = self._aliases
    if self._properties:
      data['proprties'] = self._properties
    return Serializer.to_json(data)
    # return Serializer.to_json({
    #   'subject': self._subject,
    #   'aliases': self._aliases,
    #   'properties': self._properties,
    #   'links': self._links
    # })
