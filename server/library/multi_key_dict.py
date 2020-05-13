import collections


class MultiKeyDict:
  def __init__(self, attr_keys):
    self._attr_keys = attr_keys
    self._data = {}
    self._mappings = collections.defaultdict(dict)
    self._id = 0

  def add(self, value):
    self._data[self._id] = value
    for attr_key in self._attr_keys:
      attr_value = getattr(value, attr_key)
      self._mappings[attr_key][attr_value] = self._id

  def get(self, attr_key, key):
    mapping = self._mappings[attr_key]
    return self._data[mapping[key]]
