# Write a program to check whether a number is a multiple of 3 or 5.

n = int(input("Enter number:"))

if (n % 3 == 0) and (n % 5 == 0):
    print(f"{n} is multiple of both 5 and 3")
elif(n % 5 == 0):
    print(f"{n} is multiple of 5")
elif(n % 3 == 0):
    print(f"{n} is multiple of 3")
else:
    print(f"{n} is not a multiple of 5 or 3")
