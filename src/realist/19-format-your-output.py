def list_pretty_print(items):
    for index in range(0, len(items), 5):
        if index + 5 > len(items) - 1:
            print(', '.join(str(item) for item in items[index:len(items)]))
        else:
            print(', '.join(str(item) for item in items[index:index+5]))