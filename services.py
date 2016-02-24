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
		pre_base_string = "http://api.giphy.com/v1/gifs/search?q="
		post_base_string = "&api_key=dc6zaTOxFJmzC"

		lowerCaseTerm = term.lower()
		lowerTermList = lowerCaseTerm.split()
		newStrTerm = ""
		for newStr in lowerTermList:
			newStrTerm += newStr
		newStrTerm = newStrTerm[0:-1]

		#Fetch the image url for the data.
		url = pre_base_string + newStrTerm + post_base_string
		result = urlfetch.fetch(url)

		self.response.write(str(result.content))


app = webapp2.WSGIApplication([
    (r'/', MainPage),
	(r'/sumsqnum/(\d+)', SumSquaredSequence),
	(r'/termimage/([a-z|A-Z]+)', TermImage),
], debug=True)
