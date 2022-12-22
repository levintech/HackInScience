file = open("words.txt", "r")
content = file.read()
length = len(content)

frequency_dict = {}
for letter in content:
    if letter in frequency_dict.keys():
        frequency_dict[letter] += 1
    else:
        frequency_dict[letter] = 1
        
print(frequency_dict)

for key, value in frequency_dict.items():
    print("{0}: {1:4.2f}".format(key, value / length))