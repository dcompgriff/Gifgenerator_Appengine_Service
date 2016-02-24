import webapp2
import jinja2
import os
from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'], autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		template_values = {}
		self.response.write(template.render(template_values))

class SumSquaredSequence(webapp2.RequestHandler):
	def get(self, numToSqStr):

		numToSq = long(numToSqStr)
		if numToSq > 10000000000000:
			numToSq = 10000000000000	

		self.response.write("Called sum squared text: " + str(numToSq))
		
class TermImage(webapp2.RequestHandler):
	def get(self, term):
		pre_base_string = "https://www.google.com/search?q="
		post_base_string = "&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwiq6JvAq5HLAhXJOD4KHcjmCiwQsAQIMw&biw=1366&bih=635"

		#Fetch the image url for the data.
		url = pre_base_string + term + post_base_string
		result = urlfetch.fetch(url)

		self.response.write(str(result.content))


app = webapp2.WSGIApplication([
    (r'/', MainPage),
	(r'/sumsqnum/(\d+)', SumSquaredSequence),
	(r'/termimage/([a-z]+)', TermImage),
], debug=True)
