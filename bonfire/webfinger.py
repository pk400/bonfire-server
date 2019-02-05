class Webfinger:
  def __init__(self, subject: str):
    self.subject = subject
    self._alias = None
    self._properties = None
    self._links = None
  
  @property
  def subject(self):
    return self.subject
  
  @subject.setter
  def subject(self, subject):
    prefix = 'acct:'
    if not subject.startswith(prefix):
      raise ValueError('Subject must start with "%s".' % prefix)
    subject_uri = subject[len(prefix):]

    self.subject = subject
