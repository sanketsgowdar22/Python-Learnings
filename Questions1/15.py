# Write a program to check whether a number is divisible by both 3 and 7.

n = int(input("Enter number:"))

if (n % 3 == 0) and (n % 7 == 0):
    print(f"{n} is divisble by both 3 and 7")
else:
    print(f"{n} is not divisible by both 3 and 7")
