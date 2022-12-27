from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s, key):
    encrypt_text = ''
    for character in s:
        if character in ascii_lowercase:
            encrypt_text = encrypt_text + ascii_lowercase[(ascii_lowercase.index(character) + key) % 26]
        elif character in ascii_uppercase:
            encrypt_text = encrypt_text + ascii_uppercase[(ascii_uppercase.index(character) + key) % 26]
        else:
            encrypt_text = encrypt_text + character

    return encrypt_text


def caesar_cypher_decrypt(s, key):
    decrypt_text = ''
    for character in s:
        if character in ascii_lowercase:
            decrypt_text = decrypt_text + ascii_lowercase[(ascii_lowercase.index(character) - key) % 26]
        elif character in ascii_uppercase:
            decrypt_text = decrypt_text + ascii_uppercase[(ascii_uppercase.index(character) - key) % 26]
        else:
            decrypt_text = decrypt_text + character

    return decrypt_text
