class SequenceGenerator:
  def __init__(self, initial=-1):
    self._sequence = initial

  def generate(self):
    return self._sequence + 1
