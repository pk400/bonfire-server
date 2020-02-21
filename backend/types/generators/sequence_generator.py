class SequenceGenerator:
  def __init__(self, id=-1):
    self._sequence = id

  def generate(self):
    return self._sequence + 1
