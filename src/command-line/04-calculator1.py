import sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
    elif sys.argv[2] == '+':
        print(int(sys.argv[1]) + int(sys.argv[3]))
    elif sys.argv[2] == '-':
        print(int(sys.argv[1]) - int(sys.argv[3]))
    elif sys.argv[2] == '*' or sys.argv[2] == '\*':
        print(int(sys.argv[1]) * int(sys.argv[3]))
    elif sys.argv[2] == '/':
        if sys.argv[3] == '0':
            print("input error")
        else:
            print(int(sys.argv[1]) / int(sys.argv[3]))
    elif sys.argv[2] == '%':
        print(int(sys.argv[1]) % int(sys.argv[3]))
    elif sys.argv[2] == '^':
        print(pow(int(sys.argv[1]), int(sys.argv[3])))
    else:
        print("input error")