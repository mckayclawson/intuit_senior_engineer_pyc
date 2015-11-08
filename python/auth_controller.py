"""

"""

__author__ 	= "McKay Clawson"
__email__ 	= "mckay.clawson@gmail.com"

class AuthController(RestController):

	def __init__(self, url, auths_endpoint):
		RestController.__init__()
		self.url = url
		self.auths_endpoint = auths_endpoint

	def process_ok_response(self, request):
		pass

	def process_bad_response(self, request):
		pass

	def process_response(self, request):
		if is_ok_response(request):
			process_ok_response(request):
		elif is_bad_response(request):
			process_bad_response():
		else:
			#TODO: RAISE EXCEPTION
			pass

	def get_days_availible(self):
		return self.get(self.url, self.auths_endpoint)

	def get_auths_for_day(self, day):
		endpoint = self.auths_endpoint + '/' + day
		return self.get(self.url, endpoint)




