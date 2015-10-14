import rc4
import nose
import filecmp

def test_encrypt():
	rc4.encrypt("Key", "plainfile.txt", "result.txt")
	# cipherfile.txt is verified to be correct
	assert(filecmp.cmp('cipherfile.txt', 'result.txt'))

def test_decrypt():
	rc4.decrypt("Key", "cipherfile.txt", "result.txt")
	assert(filecmp.cmp('plainfile.txt', 'result.txt'))

def test_wave_encrypt():
	rc4.encrypt("Moon", "neil.wav", "result.wav")
	# neilc.wav is verified to be correct
	assert(filecmp.cmp('neilc.wav', 'result.wav'))

def test_wave_decrypt():
	rc4.decrypt("Moon", "neilc.wav", "result.wav")
	assert(filecmp.cmp('neil.wav', 'result.wav'))

if __name__ == '__main__':
	nose.runmodule()