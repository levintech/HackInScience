from string import ascii_lowercase

for letter1 in ascii_lowercase:
    for letter2 in ascii_lowercase:
        if letter1 != letter2:
            print(letter1 + letter2)