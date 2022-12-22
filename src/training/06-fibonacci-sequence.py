def fibonacci(n):
    fib_sequence = [1, 1]
    
    if n <= 2:
        return fib_sequence[:n]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
    
    return fib_sequence