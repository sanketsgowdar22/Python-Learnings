# Write a program to check whether a number is two-digit, three-digit, or more.

n1 = int(input("Enter number 1:"))

if(9 < n1 < 99):
    print(f"The {n1} is two digit")
elif(99 < n1 < 999):
    print(f"The {n1} is three digit")
elif(n1 > 999):
    print(f"The {n1} is more than 3 digits")
else:
    print(f"{n1} is either of them")
