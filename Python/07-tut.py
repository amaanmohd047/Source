# To repeat a string 'n' times then we multiply it by n.
print("This string will be repeated 10 times." * 10)

# To avoid a new line after a print function use end=""
number = 5

print("The number is", end=" ")
print(number)

# To format a string using '.format'

str1 = "{} {} {} {} {}"

formatted_str1 = str1.format("This" , "is", "the", "formatted", "string")

print(formatted_str1)

# you can do it with using only 2 lines of code

str2 = "{} {} {} {} {} {}"

print(str2.format("This", "is", "the", "second", "formatted", "string"))

