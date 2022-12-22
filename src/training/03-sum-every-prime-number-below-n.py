from math import sqrt

def is_prime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        
        return True
    
    return False

def sum_primes(n):
    sum = 0
    for i in range(n):
        if is_prime(i):
            sum += i
    
    return sum