import requests
"""
This is a base class used to define the necessary interface between
the PYC rest service using the requests library
"""

__author__ 	= "McKay Clawson"
__email__ 	= "mckay.clawson@gmail.com"


class RestController:

	def __init__(self):
		pass

	def get(self, url, endpoint):
		return requests.get(url + endpoint)

	def is_ok_response(self, request):
		return 200 <= request.status_code < 400

	def is_bad_response(self, request):
		return 400 <= request.status_code







