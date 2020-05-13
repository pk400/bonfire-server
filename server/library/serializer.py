from library.exceptions import SerializerNotSupported


class Serializer:
  UNSUPPORTED_SERIALIZATION = 0

  @staticmethod
  def to_json(obj):
    try:
      serializer = getattr(obj, 'to_json')
      return serializer()
    except AttributeError:
      if isinstance(obj, (str, int)):
        return obj
      if isinstance(obj, dict):
        return Serializer.dict_to_json(obj)
      raise SerializerNotSupported(
        f'{obj.__class__.__name__} does not implement to_json.',
        Serializer.UNSUPPORTED_SERIALIZATION)

  @staticmethod
  def dict_to_json(obj):
    return {key: Serializer.to_json(value) for key, value in obj.items()}

  @staticmethod
  def from_json(obj, definition):
    try:
      serializer = getattr(definition, 'from_json')
      return serializer(obj)
    except AttributeError:
      if definition in [int, str]:
        return definition(obj)
      raise SerializerNotSupported(
        f'{obj.__class__.__name__} does not implement from_json.',
        Serializer.UNSUPPORTED_SERIALIZATION)
