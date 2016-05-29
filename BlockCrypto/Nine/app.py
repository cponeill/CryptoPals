def padding(data, final_len=None):
    if final_len == None:
        final_len = (len(data)/16+1)*16
    amount_to_pad = final_len - len(data)
    return data + chr(amount_to_pad) * amount_to_pad


message = 'YELLOW SUBMARINE'
padded_message = padding(message, 20)
print repr(padded_message)
