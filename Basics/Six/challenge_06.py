def keysize(key):
	for i in range(2, 40):
		if len(key) == i:
			return len(key)

key_test = 'casey' # should equal 5
#print keysize(key_test)

name_one = 'this is a test'
name_two = 'wokka wokka!!!'

from binascii import b2a_hex, a2b_hex

def test_hamming(xs, ys):
	diff = 0
	for x, y in zip(xs, ys):
		if x != y:
			diff += 1
	return diff

print test_hamming(name_one, name_two)

def count_binary_ones(xs):
	ret = 0
	while xs != 0:
		ret += 1
		xs &= xs - 1
	return ret

def hamming_distance(xs, ys):
	answer = int(b2a_hex(xs), 16) ^ int(b2a_hex(ys), 16)
	return count_binary_ones(answer)

print hamming_distance(name_one, name_two)

def repeating_xor_cipher(text, key):
	length = len(text)

	while len(key) != length:
		for i in range(len(key)):
			if len(key) == length:
				break
			key += key[i]

	ret = ("x" % (int(b2a_hex(text), 16)^int(b2a_hex(key), 16)))

	ret = "0"*(2*length-len(ret)) + ret

	return a2b_hex(ret)