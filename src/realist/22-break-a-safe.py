pair_list = []
digits = [1, 5, 8]

for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                if all(x in (a, b, c, d) for x in digits):
                    print(' '.join(str(character) for character in [a, b, c, d]))
    