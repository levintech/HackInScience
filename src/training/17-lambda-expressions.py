def filtered(items, customFilter):
    return [item for item in items if customFilter(item)]

print(*filtered(range(101), lambda x: x % 3 == 0), sep=', ')
print(*filtered(range(101), lambda x: x % 5 == 0), sep=', ')
print(*filtered(range(101), lambda x: x % 15 == 0), sep=', ')