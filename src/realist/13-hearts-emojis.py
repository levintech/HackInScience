import unicodedata

heart_list = []
for character in range(1, 230000):
    if 'HEART' in unicodedata.name(chr(character), ''):
        heart_list.append(chr(character))

print(''.join(heart_list))