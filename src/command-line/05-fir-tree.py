import sys

def firtree(tree_size):
    # Setup.
    width = 1
    minus = 2
    foot_width = 1
    space = ' '
    wood = '|'
    branch = '*'

    # Create the top of the tree, first as uncentered rows.
    rows = []
    for i in range(1, tree_size + 1):
        for j in range(1, i + 3):
            rows.append(branch * width)
            width = width + 2
        rows.append(branch * width)

        if i % 2 == 1 and i != 1:
            minus += 2
        
        width = width - minus
        
        if i % 2 == 0:
            foot_width += 2

    # Convert the rows to centered rows.
    max_width = len(rows[-1])
    centered = [
        space * (max_width // 2 - len(r) // 2) + r for r in rows
    ]

    # Build the trunk.
    trunk = [
        space * int(max_width / 2 - foot_width // 2) + wood * foot_width
        for i in range(1, tree_size + 1)
    ]

    # Profit.
    return centered + trunk

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: ./solution.py PARAM")
    elif sys.argv[1] != '0':
        size = int(sys.argv[1])
        fir = firtree(size)
        for row in fir:
            print(row)
    
    