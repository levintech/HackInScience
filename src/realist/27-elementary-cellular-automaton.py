import numpy as np
import argparse
import sys

vector = np.array([[4], [2], [1]])

def step(row, rule_binary):
    temp = np.vstack((np.roll(row, 1), row, np.roll(row, -1))).astype(np.int8)
    pattern_number = np.sum(temp * vector, axis=0).astype(np.int8)
    
    return rule_binary[7 - pattern_number]
    
def generate_automata(rule):
    rule_binary = np.array([int(_) for _ in np.binary_repr(rule, width=8)], dtype=np.int8)
        
    automata = np.zeros((40, 79), dtype=np.int8)
    automata[0, 39] = 1

    for row in range(1, 40):
        automata[row, :] = step(automata[row-1, :], rule_binary)

    output = ''
    for row in range(40):
        line = ''.join(['.' if item == 0 else '#' for item in automata[row][0:79]])
        print(line)
        output = output + line + '\n'

    return automata

if __name__ == '__main__':
    rule = int(sys.argv[1])
    generate_automata(rule)