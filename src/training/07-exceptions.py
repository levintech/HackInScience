import sys

try:
    print(sys.argv[1])
except IndexError:
    print("Not enough parameters.")