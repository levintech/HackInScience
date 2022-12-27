def bencode(input_stream):
    encoded_text = ''

    if type(input_stream) == int:
        if input_stream >= 0:
            temp_text = 'i' + str(input_stream) + 'e'
            encoded_text = encoded_text + temp_text
        else:
            temp_text = 'i' + '-' + abs(input_stream) + 'e'
            encoded_text = encoded_text + temp_text
    elif type(input_stream) == str:
        temp_text = str(len(input_stream)) + ':' + input_stream
        encoded_text = encoded_text + temp_text
    elif type(input_stream) == list:
        temp_text = 'l'
        for item in input_stream:
            temp_text = temp_text + bencode(item).decode()
        temp_text = temp_text + 'e'
        encoded_text = encoded_text + temp_text
    elif type(input_stream) == dict:
        temp_text = 'd'
        for key, value in sorted(input_stream.items(), key=lambda x: x[0]):
            temp_text = temp_text + bencode(key).decode()
            temp_text = temp_text + bencode(value).decode()
        temp_text = temp_text + 'e'
        encoded_text = encoded_text + temp_text
    
    return bytes(encoded_text, 'utf-8')
    
def entry_parser(stream, pos):
    if stream[pos].isnumeric():
        return decode_string(stream, pos)
    elif stream[pos] == 'i':
        return decode_int(stream, pos)
    elif stream[pos] == 'l':
        return decode_list(stream, pos)
    elif stream[pos] == 'd':
        return decode_dict(stream, pos)

def decode_int(stream, pos):
    pos += 1
    newPos = stream.index('e', pos)
    n = int(stream[pos: newPos])

    if stream[pos:pos + 1] == '-':
        if stream[pos + 1:pos + 2] == '0':
            raise ValueError
    elif stream[pos:pos + 1] == '0' and newPos != pos + 1:
        raise ValueError
    
    return n, newPos + 1

def decode_string(stream, pos, kind='value'):
    colon = stream.index(':', pos)
    length = int(stream[pos:colon])

    if stream[pos:pos + 1] == '0' and colon != pos + 1:
        raise ValueError

    colon += 1
    text = stream[colon:colon + length]
    
    return text, colon + length

def decode_list(stream, pos):
    content, pos = [], pos + 1

    while stream[pos:pos + 1] != 'e':
        value, pos = entry_parser(stream, pos)
        content.append(value)

    return content, pos + 1

def decode_dict(stream, pos):
    pos += 1

    content = {}

    while stream[pos:pos + 1] != 'e':
        key, pos = decode_string(stream, pos, kind='key')
        content[key], pos = entry_parser(stream, pos)

    return content, pos + 1

def bdecode(byte_stream):
    encoded_stream = byte_stream.decode()    
    data, length = entry_parser(encoded_stream, 0)
    
    return data