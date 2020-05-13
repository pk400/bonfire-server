import unittest

from library.multi_key_dict import MultiKeyDict


class MockData:
  def __init__(self, a, b, c):
    self._a = a
    self._b = b
    self._c = c

  @property
  def a(self):
    return self._a

  @property
  def b(self):
    return self._b

  @property
  def c(self):
    return self._c

  def __eq__(self, other):
    return self._a == other.a and self._b == other.b and self._c == other.c


class MultiKeyDictTester(unittest.TestCase):
  def test_something(self):
    data = MockData('z', 'x', 'y')
    multi_key_dict = MultiKeyDict(['a', 'b'])
    multi_key_dict.add(data)
    result = multi_key_dict.get('a', 'z')
    self.assertEqual(result, data)


if __name__ == '__main__':
  unittest.main()
