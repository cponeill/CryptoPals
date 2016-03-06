"""
There need to be comments explaining how this code works.
"""



# loading developer libraries
from itertools import cycle


plaintext = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
message = len("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal")
key = "ICE"

def key_loop(key, text):
	return (key * ((text/len(key))+1))[:text]

def string_xor(xs, ys):
	return "".join([chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys)])

cipher_text = string_xor(plaintext, key_loop(key, message))
hex_message = cipher_text.encode('hex')

out = ''.join(['{:02x}'.format(ord(c) ^ ord(k)) for c, k in zip(plaintext, cycle(key))])

if out == hex_message:
	print "This is the correct answer: " + hex_message