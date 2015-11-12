import hashlib
import os, base64

def getHash(password, salt=None):
	if not salt:
		salt = base64.b64encode(os.urandom(16))
	return (salt, hashlib.sha256(password+salt).hexdigest())

# Return true if user supplied password string matches hash value
def authenticate(password, hash, salt):
	# Slow down by a factor of 1million
	for count in range(1,1000000):
		getHash(password, salt)
	return hash == getHash(password, salt)[1]