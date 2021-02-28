##########   READING ###############
# to open a file 
# you can read from a file (r), write a file with some new content(w) or append the content of the file(a)

file = open("example.txt", "r")

# to check if a file is readable or not
print("The file is readable: ", file.readable())
print("The file is writable: ", file.writable())

# to read the content of a file
content = file.read()
print(content)

#to close a file # you always have to close the file once you open it
file.close()

############   WRITING ##################

file = open("example.txt", "w")

print("The file is readable: ", file.readable())
print("The file is writable: ", file.writable())

file.write("There was some text in here before i wrote this file with the text that you are now seeing")

file.close()

###########   APPENDING ####################

file = open("example.txt", "a")

print("The file is readable: ", file.readable())
print("The file is writable: ", file.writable())

file.write("\nThis is the appended text")

file.close()


######## Again reading the changes ##########

# there is a better way to do that 
# with this way you don't need to close the file
# you have to do all the operations with correct indentation

with open("example.txt", "r") as file:
    print(file.read())



######### To create a new file that doesn't exist ###########

with open("new.txt", "w") as new:
    new.write("This is the newly created file")

with open("new.txt", "r") as new:
    print(new.read())








