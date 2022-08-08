# filter function is used to filter the values according to method pass into it
# syntax = filter(method, iterator)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(a):
    return a % 2 == 0


even = tuple(filter(is_even, numbers))
print(even)

even1 = tuple(filter(lambda a: a % 2 == 0, numbers))
print(even1)

new_list = [i for i in numbers if i % 2 == 0]
print(new_list)
