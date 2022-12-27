def draw_n_squares(n):
    drawed = ''
    for row in range(2 * n + 1):
        for col in range(4 * n + 1):
            if col % 4 == 0:
                if row % 2 == 0:
                    drawed = drawed + '+'
                else:
                    drawed = drawed + '|'
            else:
                if row % 2 == 0:
                    drawed = drawed + '-'
                else:
                    drawed = drawed + ' '
        drawed = drawed + '\n'
    
    return drawed