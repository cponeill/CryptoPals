# loading developer libraries
from itertools import cycle


plaintext = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
message = len("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal")
cipher_key = "ICE"

def key_loop(text, key):
	"""
	Loops through the length of the message.
	Adds the key to the length of the message.

	text -- length of the plaintext message
	key  -- cipher key used to XOR against plaintext message

	"""
	return (key * ((text/len(key))+1))[:text]

def string_xor(text, key):
	"""
	XOR's the plainted with the key

	text -- plaintext message
	key  -- cipher key used to xor against the plaintext message
	"""
	return "".join([chr(ord(x) ^ ord(y)) for x, y in zip(text, key)])

cipher_text = string_xor(plaintext, key_loop(message, cipher_key))
hex_message = cipher_text.encode('hex')

out = ''.join(['{:02x}'.format(ord(c) ^ ord(k)) for c, k in zip(plaintext, cycle(cipher_key))])

if out == hex_message:
	print "This is the correct answer: " + hex_message