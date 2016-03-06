x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# fix the x to xs on line 5 <fixed>
# add comments
def score_plaintext(xs):
	'''Finds the score'''
	letters = filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z', xs)
	return float(len(letters)) / len(xs)

def get_max_single_char_xor(xs):
	'''loops through string and xors with the score'''
	result = []
	for i in range(256):
		chrs = [chr(ord(xs) ^ i) for xs in x.decode('hex')]
		result.append([score_plaintext(chrs), ''.join(chrs)])
	return max(result, key=lambda x: x[0])

if __name__=='__main__':
	print get_max_single_char_xor(x)