# Dictionary: Key-value pairs, Unordered, mutable, (sort of like hash table in C)

print("DEFINING A DICTIONARY:-")

d1 = {
        "name" : "Sam Alexander",
        "Universe" : "Marvel", 
        "Known as" : "Nova",
        "Hindi Version" : "Ulti Balti"
        }

print(d1)

d2 = dict(name="Cristiano Ronaldo", age="35 se jyada", jersey='07', team="Juventus(07)/Portugal(07)")

print(d2)
print("")

# To print out specific Value for a key

name1 = d1["name"]
name2 = d2["name"]

print("The name is " + name1 + ". Hayyn.")

print("The name is " + name2 + ". Hayyn.")
print("")

## To Delete an element

# Using 'del' to remove certain element

del d2["age"]

print("Age is removed now\n", d2)

# Using 'pop()' method

d1.pop("Hindi Version")
print("'Hindi Version' is popped out", d1)

# Using 'popitem()' method to remove the last added key-value pair

print("This time the last element will be popped out, i.e., 'Known as'")

d1.popitem()

print(d1)
print("")

## To check if a key is in dictionary or not

d3 = {"first" : '01', "second" : '02', "third" : '03', "fourth" : '04', "fifth" : '05'}

# By using "if....in..:" statement

if 'first' in d3:
    print(f"The Value of 'first' is: {d3['first']}.")

# By using "try:...except:..." block

try:
    print(f"The sixth value if: {d3['sixth']}.")
except:
    print("There isn't any sixth value in the Third Dictionary.")
print("")

## Looping in a Dictionary

print("All the keys in third dictionary:")
for key in d3.keys():
    print(key)

print("All the values in the third dictionary:")
for value in d3.values():
    print(value)

print("All the key-value pair in the third dictionary:")
for key, value in d3.items():
    print(f"{key} : {value}")

def lo(a):
    for key, value in a.items():
        print(f"{key} : {value}")

print("")

## To copy a dictionary

# To make a new copy use .copy() method

d4 = d3.copy()

d4['sixth'] = '06'

print('This is D3: {}'.format(d3))
print('This is D4: {}'.format(d4))

print('')

# To make a new pointer to the existing dictionary

d5 = d4

d5['zeroth'] = '00'

print('This is D4: {}'.format(d4))
print('This is D5: {}'.format(d5))

print('')

del d5
del d4['fourth']
d4['seventh'] = '07'
d3['ninth'] = '09'

## To merge two dictionaries use .update() method 
# Note: This will do kinda like a union between the dicts

print("This is d3:")
print(d3)

print("This is d4:")
print(d4)

d3.update(d4)

print("This is updated d3:")
print(d3)
print('')

## Immutable Objects can be used as keys in Dictionaries

d6 = {1:'one', 2:'two', 3:'three'}

print('The new dictionary D6 is:')
lo(d6)

d7 = {(1, 2):'3', (3, 4):'7', (5, 6):'11'}

print('The new dictionary D7 tells sum of the numbers:')
lo(d7)

## Unhashable types cannot be used as keys, e.g., 

try:
    li = [7, 8]
    d8 = {li: "Sum is 15"}
except:
    print("Error\nLists cannot be used as keys since they are mutable after creation.")

