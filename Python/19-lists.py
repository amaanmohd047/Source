# List : mutable, ordered, allows duplicate elements

# we can use this function to  iterate over the list
def prlist(name):
    for item in name:
        print(f"{item}", end=" ")


# A list can be defined by [] or list

list1 = ["This", "is", "the", "first", "list", "."]

print(list1)

prlist(list1)

list3 = ["This", "is", 'second', 'list']


# To Create an empty list
new_list = []

# OR
new_list2 = list()
list2 = list()

print(new_list2, new_list)

# To refernce a particular item in a list

first_word_of_list1 = list1[0]

print('The first word of the first list is : "{}"'.format(first_word_of_list1))

second_word_of_list1 = list1[1]

print('The second word of the first list is : "{}"'.format(second_word_of_list1))

last_word_of_list1 = list1[-1]

print('The last word of the first list is : "{}"'.format(last_word_of_list1))

second_last_word_of_list1 = list1[-2]

print('The second last word of the first list is : "{}"'.format(second_last_word_of_list1))

# To check whether an item is in the list or not 

if "list" in list1:
    print('The word "list" is in the first list.')
else:
    print('The word "list" is not present in the first list.')

if "Foo" in list1:
    print('The word "Foo" is in the first list.')
else:
    print('The word "list" is not present in the first list.')


# To check the length of the list

print("The length of list1 is {}.".format(len(list1)))
print("The length of list2 is {}.".format(len(list2)))
print("The length of list3 is {}.".format(len(list3)))

# To append items in the list 

list2.append(list3)

prlist(list2)

# Here list3 is an item of list2

list3.append('.')

prlist(list2)

list2.append(['This', 'is', 'another', 'item', 'in', 'the', 'list', '.'])

prlist(list2)

# To insert an item in a list at a certain index
list3.insert(2, "the")

prlist(list2)

# To remove last item from the list and return it

removed_item1 = list1.pop()

print('The removed item is : "{}"'.format(removed_item1))

print('The remaining list is : \n"{}"'.format(list1))

# To remove a certain element from the list

list1.remove("is")

print(list1)

# To remove all elements from a list

list1.clear()

print(list1)

# To reverse a list use reverse()

list3.reverse()

print(list3)

# To sort a list u can use "list.sort()" or "variable = sorted(list)"

list3.sort()

prlist(list3)


#######################################
list4 = [23, 78, 45, -89, -8, 458, 98]#
#######################################

sorted_list4 = sorted(list4)
print(list4)
print(sorted_list4)

########################################################
list5 = ["This will be in the list five times.\n"] * 5 #
########################################################                                                    

prlist(list5)














