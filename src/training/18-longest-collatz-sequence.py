def collatz_length(n):
    length = 0
    
    while n != 1:
        length += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    
    return length

print(10)