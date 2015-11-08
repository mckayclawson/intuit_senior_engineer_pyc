import paramiko
"""

"""

__author__ 	= "McKay Clawson"
__email__ 	= "mckay.clawson@gmail.com"

class SftpController():

	def __init__(sftp_server, sftp_user, private_key_file, private_key_password):
		self.private_key = paramiko.RSAKey.from_private_key_file(private_key_file, password = private_key_password)
		self.sftp_user = sftp_user
		self.sftp_server = sftp_server

	def get_sftp_client(self):
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname = self.sftp_server, username = self.sftp_user, pkey = self.private_key)
		return ssh_client.open_sftp()

	#TODO:this doesn't close the underlying ssh_client, do the needful
	def close_sftp_client(self, sftp_client):
		sftp_client.close()

	def get_file(self, remote_filepath, local_filepath):
		sftp_client = get_sftp_client()
		#TODO: add eception handling
		sftp_client.get(remote_filepath, local_filepath, callback = None)
		sftp_client.close()

	def remove_file(self, remote_filepath):
		sftp_client = get_sftp_client()
		#TODO: catch IOError
		sftp_client.remove(remote_filepath)
		sftp_client.close()

	def list_directory(self, directory):
		sftp_client = get_sftp_client()
		contents = sftp_client.listdir(path = directory)
		sftp_client.close()

	




	



