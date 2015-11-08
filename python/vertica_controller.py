import pyodbc
import os
import subprocess
import SafeConfigParser

"""

"""

__author__ 	= "McKay Clawson"
__email__ 	= "mckay.clawson@gmail.com"


class VerticaController():

	def __init__(vsql_config_file):
		vsql_config = init_vsql_config_parser(vsql_config_file)
		self.hostname = vsql_config['host']
		self.uname = vsql_config['username']
		self.env = dict(os.environ)
		self.env['VSQL_PASSWORD'] = vsql_config['password'].replace("'", "")
		self.connectionString = 'vsql -U ' + self.uname + ' -h ' + self.hostname 

	def executeSqlQuery(self, query):
		#TODO Error Handling
		executeString = self.connectionString + ' -c \'' + query + '\' -v ON_ERROR_STOP=on'
		text = subprocess.check_output(executeString, env=self.env, shell=True)
		return text

	def executeSqlFile(self, filename):
		#TODO Error Handling
		executeString = self.connectionString + ' -At -f ' + filename + ' -v ON_ERROR_STOP=on'
		text = subprocess.check_output(executeString, env=self.env, shell=True)
		return text

def init_vsql_config_parser(self, vsql_config_file):
	config_parser = SafeConfigParser()
	config_parser.optionxform = str
	config_parser.read(vsql_config_file)
	ret_map = {}
	for (key,value) in config_parser.items('vsql_config'):
			ret_map[key] = value
	return ret_map