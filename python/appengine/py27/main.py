import webapp2
from google.appengine.dist import use_library
use_library('django', '1.2')

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, WebApp World!')

application = webapp2.WSGIApplication([('/', MainPage)])
