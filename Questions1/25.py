# Write a program to check whether a number is divisible by 2 but not by 5.

n = int(input("Enter number:"))

if(n % 2 == 0):
    if(n % 5 != 0):
        print(f"The {n} is divisible by 2 but not by 5")
else:
    print(f"The {n} is not divisible either of them")
