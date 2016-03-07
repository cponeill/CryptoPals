# Fixed XOR

string_one = '1c0111001f010100061a024b53535009181c'
string_two = '686974207468652062756c6c277320657965'

answer_a = string_one.decode('hex')
answer_b = string_two.decode('hex')

def fixed_xor(one, two):
	'''XOR's two strings together'''
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(one, two))

my_answer = fixed_xor(answer_a, answer_b).encode('hex')
print my_answer
# answer = '746865206b696420646f6e277420706c6179'