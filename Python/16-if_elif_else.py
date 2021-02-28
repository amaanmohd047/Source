# if-elif-else condition :-

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    print(num1, "is greater than ", num2, ".")
elif num1 < num2:
    print(num1, "is smaller than", num2, ".")
else:
    print("Both numbers are the same.")
