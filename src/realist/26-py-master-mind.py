import string
import random
import itertools

def gen_colors(code_size):
    length = code_size if code_size < 26 else 26
    return string.ascii_uppercase[:length]

def gen_code(code_size, colors):
    return ''.join(random.choices(colors, k=code_size))

def check_guess(guess, code_size, colors):
    return len(guess) == code_size and all(color in colors for color in guess)

def score_guess(code, guess):
    length = len(code) if len(code) < len(guess) else len(guess)
    right_position = 0
    wrong_position = 0
    
    filtered_code = ''
    filtered_guess = ''
    for index in range(length):
        if code[index] == guess[index]:
            right_position += 1
        else:
            filtered_code = filtered_code + code[index]
            filtered_guess = filtered_guess + guess[index]
    
    unique_code = ''.join(color for color, _ in itertools.groupby(filtered_code))
    unique_guess = ''.join(color for color, _ in itertools.groupby(filtered_guess))
    wrong_position = len(set(unique_code) & set(unique_guess))
    
    return right_position, wrong_position

def play_cli(code_size, nb_colors):
    colors = gen_colors(nb_colors)
    code = gen_code(code_size, colors)
    print("Possible colors are ", colors)
    print("Code is size {}.".format(code_size))
    print("CODE = ", code)
        

if __name__ == '__main__':
    play_cli(4, 6)