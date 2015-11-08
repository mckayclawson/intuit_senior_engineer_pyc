from auth_controller import AuthController
from data_controller import DataController
from sftp_controller import SFTPController
from etl import ETL

"""

"""
__author__ 	= "McKay Clawson"
__email__ 	= "mckay.clawson@gmail.com"

def run_etl():
	#initialize auth_controller
	auth_controller = AuthController('http://restservice:8001/ETL/api/v1.0/', 'auths')

	#initialize data_controller
	data_controller = DataController('http://restservice:8001/ETL/api/v1.0/')

	#initialize sftp_controller
	sftp_controller = SftpController('sftpserver.pyc.test', 'etluser', 'sftpserver_keys/sftpserver_rsa', 'IntuitPYC')

	#initialize vertica_controller

	vertica_controller = VerticaController('config/vsql.config')

	etl = ETL(auth_controller, data_controller, sftp_controller, vertica_controller)
	etl.run()






if __name__ == "__main__":
	run_etl()