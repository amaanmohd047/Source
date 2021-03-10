# filter is a built-in fuction in python which is used to filter the elemnts in the iterable according to the function

# Usage: filter(func, *iterable)

tup = (1, 2, 3, 4, 5, 6, 7, 8)

non_even = filter(lambda a: a%2 != 0, tup)

print(non_even)

# Just like map, to print non_even we need to cast it into set or list or tuple

print(set(non_even))

non_even = filter(lambda a: a%2 != 0, tup)

print(list(non_even))

non_even = filter(lambda a: a%2 != 0, tup)

print(tuple(non_even))
