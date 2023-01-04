import numpy as np


def dirichlet_square_solver(square):
    while True:
        b = True
        for i in range(1, square.shape[0]-1):
            for j in range(1, square.shape[1]-1):
                a = (square[i-1][j] + square[i+1][j] + square[i][j-1] + square[i][j+1]) / 4
                c = (square[i-1][j] + square[i+1][j] + square[i][j-1] + square[i][j+1]) % 4
                if (c != 0):
                    square[i][j] = a + 1
                    b = False
                elif (square[i][j] < a):
                    square[i][j] = a
                    b = False
                else:
                    continue
        print(square)
        if b: break