#!/usr/bin/python

import urllib
import urllib2

class restClient:
	def __init__(self):
		self.headers = {}
		self.opener = urllib2.build_opener(urllib2.HTTPHandler)

	def buildRequest(self, url, method, payload={}):
		payload = urllib.urlencode(payload)
		request = urllib2.Request(url, data=payload)
		# If we have custom headers,
		# we add them to the request
		if request:
			for key, value in self.headers.items():
				request.add_header(key, value)
			# Reset the class headers
			self.headers = {}

		# Set the custom method to the request
		request.get_method = lambda: method
		self.httpRsc = self.opener.open(request)

	def getResponse(self):
		return self.httpRsc.read()

	def setHeaders(self, headers={}):
		self.headers = headers

	# Make a GET request
	def get(self, url, data={}):
		if data != None:
			url = url + '?' + urllib.urlencode(data)
		self.buildRequest(url, "GET")
		return self.getResponse()

	# Make a POST request
	def post(self, url, data={}):
		self.buildRequest(url, "POST", data)
		return self.getResponse()

	# Make a PUT request
	def put(self, url, data={}):
		self.buildRequest(url, "PUT", data)
		return self.getResponse()

	# Make a DELETE request
	def delete(self, url, headers={}):
		self.buildRequest(url, "DELETE")
		return self.getResponse()

