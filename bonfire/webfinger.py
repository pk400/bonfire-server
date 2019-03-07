from typing import List, Dict

from starlette.applications import Starlette

class Webfinger:
  def __init__(self, subject: str):
    self._subject = subject
    self._alias = None
    self._properties = None
    self._links = None
  
  @property
  def subject(self):
    return self._subject
  
  @subject.setter
  def subject(self, subject: str):
    self._subject = subject
  
  @property
  def alias(self):
    return self._alias
  
  @alias.setter
  def alias(self, alias: List[str]):
    self._alias = alias

  @property
  def properties(self):
    return self._properties
  
  @properties.setter
  def properties(self, properties: Dict):
    self._properties = properties

def WebfingerAsgi():
  app = Starlette()

  @app.route('/')
  def on_resource(request):
    pass

  return app
