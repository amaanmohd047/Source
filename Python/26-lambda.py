# If i have to add 21 to a number i can make a function for that like:

def add21_func(x):
    return x + 21

print(add21_func(79))

# In python we can do this in just one line

add21 = lambda x: x + 21

print(add21(7))

# We can take two arguments too with a lambda function

divide = lambda x,y: x/y

q = int(input("> "))
w = int(input('(!= 0) > '))

print(divide(q,w))
