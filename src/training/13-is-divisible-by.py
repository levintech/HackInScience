for number in range(0, 1001):
    if number % 7 == 0:
        if sum([int(item) for item in str(number)]) % 3 == 0:
            print(number)