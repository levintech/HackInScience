from math import sqrt

def is_prime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        
        return True
    
    return False

def print_prime(valueRange):
    prime_list = []
    for i in range(valueRange[0], valueRange[1]):
        if is_prime(i):
            prime_list.append(i)
    
    print(*prime_list, sep = ', ')


print_prime([10000, 10050])