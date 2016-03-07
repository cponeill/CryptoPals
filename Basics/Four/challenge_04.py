from challenge_03 import get_max_single_char_xor

def xor_answer():
	"""
	Imports function from challenge_03
	loops through text file to find key
	returns XOR'd text. 

	"""
	result = []
	with open('file.txt', 'r') as f:
		for line in f.readlines():
			result.append(get_max_single_char_xor(line))
	return max(result, key=lambda x: x[0])

if __name__=='__main__':
	print xor_answer()