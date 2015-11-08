"""

"""

__author__ 	= "McKay Clawson"
__email__ 	= "mckay.clawson@gmail.com"

class DataController(RestController):

	def __init__(self, url):
		RestController.__init__()
		self.url = url

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

	def advance(self):
		return self.get(url, 'advance')

	def reset(self):
		return self.get(url, 'reset')

