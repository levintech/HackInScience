from math import sqrt

def is_prime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        
        return True
    
    return False
    
def next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            break
        n += 1
    print(n)

next_prime(100000000)