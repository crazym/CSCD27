import hashlib

def getHash(password):
	return hashlib.sha256(password).hexdigest()

# Return true if user supplied password string matches hash value
def authenticate(password, hash):
    return hash == getHash(password)