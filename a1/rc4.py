#!/usr/bin/env python
import wave

# Takes a key and input text and output the scrambled text
def crypt(key, text):
	s = create_key_schedule(key)
	i=0
	j=0
	output=[]
	for m in text:
		i = (i+1) % 256
		j = (j+ s[i]) % 256
		s[i], s[j] = s[j], s[i]
		t = (s[i]+s[j]) % 256
		output.append(chr(ord(m) ^ s[t]))
	return output

# Encrypt the plainfile with the key and ouput to cipherfile using RC4
def encrypt(key, plainfile, cipherfile):

	if plainfile.endswith('.wav'):
		# Wave file
		waveRead = wave.open(plainfile, 'rb')
		waveWrite = wave.open(cipherfile, 'wb')

		# Reads the parameters
		header = waveRead.getparams()
		frames = waveRead.getnframes()
		sampleWidth = waveRead.getsampwidth()
		assert(waveRead.getnchannels() == 1)

		plaintext = [byte for byte in waveRead.readframes(frames)]
		ciphertext = bytearray([x for x in crypt(key, plaintext)])

		# Writes the parameters and data to wave
		waveWrite.setparams(header)
		waveWrite.setnchannels(1)
		waveWrite.setsampwidth(sampleWidth)
		waveWrite.writeframes(ciphertext)

		waveRead.close()
		waveWrite.close()

	else:
		# Regular file
		with open(plainfile) as plainTextFile:
			with open(cipherfile, mode='w') as cipherTextFile:
				plaintext = plainTextFile.read()
				ciphertext = ''.join(crypt(key, plaintext))
				cipherTextFile.write(ciphertext)

# Decrypt the cipherfile with the key and ouput to decryptfile using RC4
def decrypt(key, cipherfile, decryptfile):
	if cipherfile.endswith('.wav'):
		# Wave file open
		waveRead = wave.open(cipherfile, 'rb')
		waveWrite = wave.open(decryptfile, 'wb')

		# Reads the parameters
		header = waveRead.getparams()
		frames = waveRead.getnframes()
		sampleWidth = waveRead.getsampwidth()
		assert(waveRead.getnchannels() == 1)

		ciphertext = [byte for byte in waveRead.readframes(frames)]
		plaintext = bytearray([x for x in crypt(key, ciphertext)])

		# Writes the parameters and data to wave
		waveWrite.setparams(header)
		waveWrite.setnchannels(1)
		waveWrite.setsampwidth(sampleWidth)
		waveWrite.writeframes(plaintext)

		waveRead.close()
		waveWrite.close()

	else:
		# Regular file
		with open(cipherfile) as cipherTextFile:
			with open(decryptfile, mode='w') as plainTextFile:
				ciphertext=cipherTextFile.read()
				plaintext = ''.join(crypt(key, ciphertext))
				plainTextFile.write(plaintext)

# Creates the key stream for RC4, given a key
def create_key_schedule(key):
	s=[]
	t=[]
	for i in range(0,256):
		s.append(i)
		t.append(ord(key[i % len(str(key))]))

	j=0
	for i in range(0,256):
		j = (j + s[i] + t[i]) % 256
		s[i], s[j] = s[j], s[i]
	return s


# if __name__=="__main__":
# 	encrypt("Key", "plainfile.txt", "cipherfile.txt")
# 	decrypt("Key", "cipherfile.txt", "decryptfile.txt")
# 	encrypt("Moon", "neil.wav", "neilc.wav")
# 	decrypt("Moon", "neilc.wav", "cipherfile.wav")