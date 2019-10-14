import abc

class DataStore:
  def __init__(self):
    self._is_open = False

  @abc.abstractmethod
  def open(self):
    raise NotImplementedError()

  @abc.abstractmethod
  def close(self):
    raise NotImplementedError()
