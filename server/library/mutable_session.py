class MutableSession:
  def __init__(self):
    self._is_modified = False

  @property
  def is_modified(self):
    return self._is_modified

  def update_state(self):
    if not self._is_modified:
      self._is_modified = True

  def reset_state(self):
    self._is_modified = False
