# Convert hex to base64

# load developer library
import binascii

my_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hex_to_base64(string):
	hex = string.decode('hex')
	base = binascii.b2a_base64(hex)
	return base

print hex_to_base64(my_string)

# answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'