def sort_by_mark(my_class):
    return sorted(my_class, key=lambda x: x[0], reverse=True)


def sort_by_name(my_class):
    return sorted(my_class, key=lambda x: x[1])


# Uncomment the following lines as needed
# if you want to test your implementation a bit:

# my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

# print(sort_by_mark(my_class))
# print(sort_by_name(my_class))