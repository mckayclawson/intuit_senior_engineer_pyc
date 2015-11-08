
"""

"""

__author__ 	= "McKay Clawson"
__email__ 	= "mckay.clawson@gmail.com"

class ETL():

	def __init__(auth_controller, data_controller, sftp_controller vertica_controller):
		self.auth_controller = auth_controller
		self.data_controller = data_controller
		self.sftp_controller = sftp_controller
		self.vertica_controller = vertica_controller

	def advance_day(self):
		data_controller.advance()

	def reset_days(self):
		data_controller.reset()

	#may not be necessary, given the reliability of the sftp server 
	#i.e. if you call advance the file is there
	#although in real life you would have to poll for the file
	def poll_for_clickstream_file(self):

