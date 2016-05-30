# Loading Devloper Libraries
from Crypto.Cipher import AES
from Crypto import Random
from random import randint
from binascii import a2b_base64

# Function to generate a random key
def random_key(length=16):
    return ''.join(chr(randint(0,255)) for i in range(length))

# Function tht loops through 'xs' and xors xs and ys together.
# To be used in CBC functin
def xor(xs, ys):
    return ''.join(chr(ord(xs[i]) ^ ord(ys[i])) for i in range(len(xs)))

# Function takes two arguments (data, key)
# Encrypts data to key using the Electronic Codebook blockcipher
def AES_ECB(data, key, pad=False):
    cipher = AES.new(key, AES.MODE_ECB)
    if pad:
        data = pcks7_padding(data)
    return cipher.encrypt(data)

# Function that uses PCKS7 padding algorithm
def pcks7_padding(data, final_len=None):
    if final_len == None:
        final_len = (len(data)/16 + 1)*16
    amount_to_pad = final_len - len(data)
    return data + chr(amount_to_pad) * amount_to_pad


# Function takes three arguments (data, key, iv)
# Returns data using Cipher Block Chaining mode. 
# Key is generated from random_key()
def AES_CBC(data, key, iv):
    iv = pcks7_padding(data)
    block_count = len(data)/16
    encrypted_data = ''
    prev_block = iv
    for b in range(block_count):
        cur_block = data[b*16:(b+1)*16]
        encrypted_block = AES_ECB(xor(cur_block, prev_block), key)
        encrypted_data += encrypted_block
        prev_block = encrypted_block
    return encrypted_data


tester = 'UNINITIALIZED'

# Encryption Oracle
def encryption_oracle(data):
    global tester
    should_encrypt_CBC = (randint(0,1)==0)
    key = random_key()

    data = random_key(randint(5,10)) + data + random_key(randint(5,10))

    if should_encrypt_CBC:
        iv = random_key()
        tester = "CBC"
        return AES_CBC(data, key, iv)

    else:
        tester = "ECB"
        return AES_ECB(data, key, True)

def is_ecb_encoded(data, block_size):
    block_count = len(data)/block_size
    for i in range(block_count):
        for j in range(i+1, block_count):
            if data[i*block_size:(i+1)*block_size] == data[j*block_size:(j+1)*block_size]:
                return True
    return False

def identify_ECB_or_CBC(oracle):
    block_length = 16
    plain_text  = 'A'*(3*block_length)
    cipher_text = oracle(plain_text)
    if is_ecb_encoded(cipher_text, 16):
        return "ECB"
    else:
        return "CBC"


for i in range(256):
    is_ECB = identify_ECB_or_CBC(encryption_oracle)
    if is_ECB != tester:
        print("YES")
    else:
        print("NO")
