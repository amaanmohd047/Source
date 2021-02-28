# Tuples: Ordered, Immutable, allows duplicate elements

import random as rd

tup1 = ("Cristiano", "Ronaldo", "07")

print(tup1)

for i in tup1:
	print(i)

if "Donald" in tup1:
	print("Yes, Donaldo is in the tuple.")
else:
	print("No, Donald is not in the tuple.")

###################

# Tuple can also be defined by typecasting.

tup2 = tuple(['xavi', 'iniesta', 'fabregas', 'villa', 'torres'])

# To print the length of a tuple

print(len(tup2))

print(f"Who is the random in them: {rd.choice(tup2)}")

# To count the no of specific element in the tuple

print("The no. of Xavi(s) in the team is/are: ", tup2.count('xavi'))

# To find the index of specific element in the tuple

print("The index where Villa is is: ", tup2.index('villa'))

#######g#####################

tup3 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing of Tuple can be done in many ways as needed

print("The tuple can be sliced too. e.g. ,")

print(tup3[2:6])

print(tup3[:5])

print(tup3[6:])

print(tup3[2:8:2])

print("")

# A list or tuple can be reversed by using string slicing 

print("The tuple can be reversed by using slicing")

print(tup3[::-1])

####################

# Unpacking a tuple

tup4 = tuple(["Sam", "Alexander", "Nova", "Ulti Balti"])

first_name, surname, known_as, hindi_version = tup4

print("")

print("Unpacking a tuple")

print(first_name)

print(surname)

print(known_as)

print(hindi_version)

# Use "*" for unpacking the rest of the elements

tup5 = tuple([23, 21, 53, 255, 24, 353])

print("The fifth tuple is:\n", tup5)

first_num, *rest_num, last_num = tup5

print("The first number of the fifth tuple is: ", first_num)

print("The last number of the fifth tuple is: ", last_num)

print("The rest of the numbers of the fifth tuple are:", rest_num)
