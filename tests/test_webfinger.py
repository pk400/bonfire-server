import unittest

from bonfire.webfinger import Webfinger

class TestWebfinger(unittest.TestCase):
  def test_create(self):
    subject = 'acct:a@x.com'
    try:
      wf = Webfinger(subject)
    except ValueError:
      self.fail('Could not create Webfinger for: %s' % subject)
