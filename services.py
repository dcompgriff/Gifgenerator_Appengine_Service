import webapp2
import jinja2
import os
import random
import json
from google.appengine.api import urlfetch
from google.appengine.api import memcache

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'], autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		template_values = {}
		self.response.write(template.render(template_values))
		
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

		#Check memcache for image url.
		client = memcache.Client()
		strCachedUrl = client.get(newStrTerm)
		if strCachedUrl is not None:
			returnObject = {"url": strCachedUrl}
			self.response.write(json.dumps(returnObject))	
		else:				
			#Fetch the image url for the data.
			url = pre_base_string + newStrTerm + post_base_string
			result = urlfetch.fetch(url)

			#Store the url in memcache.
			returnObject = {"url": ""}
			giphyObject = json.loads(str(result.content))
			if len(giphyObject["data"]) == 0:
				client.add(newStrTerm, "", 60)
				self.response.write(json.dumps(returnObject))
			else:
				imageIndex = random.randint(0, len(giphyObject["data"]) - 1)
				returnObject["url"] = giphyObject["data"][imageIndex]["images"]["fixed_height"]["url"]
				client.add(newStrTerm, returnObject["url"], 60)
				self.response.write(json.dumps(returnObject))


app = webapp2.WSGIApplication([
    (r'/', MainPage),
	(r'/termimage/([a-z|A-Z]+)', TermImage),
], debug=True)
