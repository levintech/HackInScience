import random
import numpy as np

def init_grid():
    grid = np.zeros((4, 4), dtype=int)
    
    r1 = random.randint(0, 3)
    c1 = random.randint(0, 3)
    grid[r1][c1] = 2

    r2 = random.randint(0, 3)
    c2 = random.randint(0, 3)
    while r1 == r2 and c1 == c2:
        r2 = random.randint(0, 3)
        c2 = random.randint(0, 3)
        
    grid[r2][c2] = 2
    
    return grid

def add_new(grid):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while grid[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    if random.randint(0, 9) < 8:
        grid[r][c] = 2
    else:
        grid[r][c] = 4
    
    return grid

def rollin_row(row):
    new_row = [0] * 4
    temp_row = [0] * 4

    # compress
    pos = 0
    for i in range(4):
        if row[i] != 0:
            temp_row[pos] = row[i]
            pos += 1

    # merge
    for i in range(3):
        if temp_row[i] == temp_row[i + 1] and temp_row[i] != 0:
            temp_row[i] = temp_row[i] * 2
            temp_row[i + 1] = 0

    # compress
    pos = 0
    for i in range(4):
        if temp_row[i] != 0:
            new_row[pos] = temp_row[i]
            pos += 1
    
    return new_row

def rollin(grid, direction):
    new_grid = []

    if direction == 'r':
        grid = reverse(grid)

        for row in grid:
            new_row = rollin_row(row)
            new_grid.append(new_row)
        new_grid = reverse(new_grid)

        return new_grid
    elif direction == 'u':
        grid = transpose(grid)

        for row in grid:
            new_row = rollin_row(row)
            new_grid.append(new_row)

        new_grid = transpose(new_grid)
        return new_grid
    elif direction == 'd':
        grid = transpose(grid)
        grid = reverse(grid)

        for row in grid:
            new_row = rollin_row(row)
            new_grid.append(new_row)
        
        new_grid = reverse(new_grid)
        new_grid = transpose(new_grid)
        return new_grid
    else:
        for row in grid:
            new_row = rollin_row(row)
            new_grid.append(new_row)
        return new_grid

def reverse(grid):
    new_grid = np.zeros((4, 4), dtype=int)
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][3 - j]
    
    return new_grid

def transpose(grid):
    new_grid = np.zeros((4, 4), dtype=int)
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[j][i]
    
    return new_grid

def get_current_state(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return 'WON'
    
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return 'GAME NOT OVER'
    
    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]:
                return 'GAME NOT OVER'
    
    for j in range(3):
        if grid[3][j] == grid[3][j + 1]:
            return 'GAME NOT OVER'

    for i in range(3):
        if grid[i][3] == grid[i + 1][3]:
            return 'GAME NOT OVER'
    
    return 'LOST'


def my2048():
    grid = init_grid()

    while True:
        command = input()

        if command in ['l', 'r', 'u', 'd']:
            grid = rollin(grid, command)
            status = get_current_state(grid)
            print(status)
            if status == 'WON':
                print("Congrats! You Win.")
                break
            elif status == 'LOST':
                print("Game Over ! :(")
                break
            add_new(grid)
        elif command:
            print("Unknown command.")
            print("Press l, r, u or d + Enter")