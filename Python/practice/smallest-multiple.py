# Question :-
#           2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#           What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Solution :-

def sol():
    num = 1
    while True:
        if (num % 20 == 0 and num % 19 == 0 and num % 18== 0 and num % 17== 0 and num % 16 == 0 and num % 15== 0 and num % 14== 0 and num % 13== 0 and num % 12== 0 and num % 11== 0):
            print("The Number is : ", num)
            break
        num = num + 1

if __name__ == "__main__":
    sol()
