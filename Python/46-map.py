# map is a built-in function in python which is used to map an iterable as defined by the function

## Usage: map(func, *iterable) --> map object

x = [2, 4, 6, 8, 10, 12]

c = map(lambda a: a/2, x)

print(c)

# To print the value of c we need to cast c into a set or list or tuple

print(set(c))

c = map(lambda a: a/2, x)

print(tuple(c))

c = map(lambda a: a/2, x)

print(list(c))
