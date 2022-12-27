import string
import random

def pwgen(length, with_digits=True, with_uppercase=True):
    if with_digits and with_uppercase:
        while True:
            psw = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=length))
            if any(character in string.ascii_lowercase for character in psw) and any(character in string.digits for character in psw) and any(character in string.ascii_uppercase for character in psw):
                return psw
    elif with_digits:
        while True:
            psw = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
            if any(character in string.ascii_lowercase for character in psw) and any(character in string.digits for character in psw):
                return psw
    elif with_uppercase:
        while True:
            psw = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=length))
            if any(character in string.ascii_lowercase for character in psw) and any(character in string.ascii_uppercase for character in psw):
                return psw
    
    return ''.join(random.choices(string.ascii_lowercase, k=length))