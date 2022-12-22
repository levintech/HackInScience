from math import factorial

def print_pascal_triangle(height):
    for i in range(height):
        for j in range(height-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        
        print()