class ServiceType:
  NOT_OPEN = 0

  def __init__(self):
    self._is_open = False

  @property
  def is_open(self):
    return self._is_open

  def startup(self):
    raise NotImplementedError()

  def shutdown(self):
    raise NotImplementedError()

  def open(self):
    self.startup()
    self._is_open = True
  
  def close(self):
    self.shutdown()
    self._is_open = False
