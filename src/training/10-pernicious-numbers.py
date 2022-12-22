from math import sqrt

def is_prime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        
        return True
    
    return False

for number in range(222281, 222381):
    if is_prime(bin(number).count('1')):
        print(number)