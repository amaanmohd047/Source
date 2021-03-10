# sorted(arg, key)

list1 = [23, 42, 11, 24, 92, 435]

# We can sort any thing in python using sorted

print(sorted(list1))

# Sorted() takes a key to decide the basis of sorting else it sorts on the first element

l2 = [(2, 4, 5), (1, -4, 5), (8, -2, -4)]

print(sorted(l2))

print(sorted(l2, key = lambda x: x[1]))

print(sorted(l2, key = lambda x: x[2]))

print(sorted(l2, key = lambda x: x[0] + x[1] + x[2]))
