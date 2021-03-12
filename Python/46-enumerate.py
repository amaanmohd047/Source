# enumerate returns index and item from the list

list1 = ["Hello", "this", "is", "a", "list", "."]

for i, word in enumerate(list1):
    if i%2 == 0:
        print(f"The selected word is {word}")
