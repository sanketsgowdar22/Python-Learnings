# Write a program to find the largest among three numbers using nested if.

n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
n3 = int(input("Enter number 3:"))

if(n1 > n2):
    if(n1 > n3):
        print(f"The {n1} is greater.")
    else:
        print(f"The {n3} is greater.")
elif(n2 > n1):
    if(n2 > n3):
        print(f"The {n2} is greater.")
    else:
        print(f"The {n3} is greater.")
else:
    print(f"The {n3} is greater")
