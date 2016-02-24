import webapp2
import jinja2
import os
import urllib

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
		self.response.write("Received Term: " + str(term))


app = webapp2.WSGIApplication([
    (r'/', MainPage),
	(r'/sumsqnum/(\d+)', SumSquaredSequence),
	(r'/termimage/([a-z]+)', TermImage),
], debug=True)
