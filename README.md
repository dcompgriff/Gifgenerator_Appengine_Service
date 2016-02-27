hw3_appengine_services
======================
Service URL: http://hw3-cloud-comp.appspot.com

Service Overview
======================
This service accepts a term, and uses that term to query a set of animated gifs using the google url fetch service. After retrieving the set of gifs, the service randomly selects one gif url to return, and caches the url in google's memcache service for a minute. If the same term is queried multiple times, the cached result is returned instead of calling the giphy api again. The web service was written using the webapp2 framework, along with the jinga2 template framework. It has 2 main urls. The "/" index url serves an html index template that has inline javascript and JQuery code. When a user clicks the submit button, the "/termimage/<term>" is called with a get request. This causes the backend service to query the public giphy API, and parse through the result.

Installation
======================
To run this service on your own machine, download python 2.7, the webapp2 python package, and the google python sdk. The git repo can be cloned from the uc github site, and run using dev_appserver.py hw3_appengine_services/. 

Appengine Services Used
======================
1.) Google Memcache
url: https://cloud.google.com/appengine/docs/python/memcache/usingmemcache
2.) Google Url Fetch
url: https://cloud.google.com/appengine/docs/python/urlfetch/











