# the most popular example of recursion is Factorial Function

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)


def main():
    number = int(input("Enter the number: "))
    factorial = fact(number)
    print(f"The Factorial of {number} is {factorial}")

if __name__ == "__main__":
    main()

