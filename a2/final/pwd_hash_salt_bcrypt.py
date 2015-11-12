import bcrypt

def getHash(password, salt=None):
	if not salt:
		salt = bcrypt.gensalt()
	return (salt, bcrypt.hashpw(password, salt))

# Return true if user supplied password string matches hash value
def authenticate(password, hash, salt):
   	return hash == getHash(password, salt)[1]