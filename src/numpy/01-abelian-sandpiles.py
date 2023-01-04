import numpy as np

def iterate(sandpile):
    changed = False
    for ii, arr in enumerate(sandpile):
        for jj, val in enumerate(arr):
            if val > 3:
                sandpile[ii, jj] -= 4
                if ii > 0:
                    sandpile[ii - 1, jj] += 1
                if ii < len(sandpile)-1:
                    sandpile[ii + 1, jj] += 1
                if jj > 0:
                    sandpile[ii, jj - 1] += 1
                if jj < len(sandpile)-1:
                    sandpile[ii, jj + 1] += 1
                changed = True
    return sandpile, changed

def apply_gravity(sandpile):
    while True:
        grid, changed = iterate(sandpile)
        if not changed:
            break
        
