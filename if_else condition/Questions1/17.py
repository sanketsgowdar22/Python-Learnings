# Write a program to find the largest of three numbers.

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
n3 = int(input("Enter n3:"))

if(n1 > n2) and (n1 > n3):
    print(f"{n1} is greater.")
elif(n2 > n1) and (n2 > n3):
    print(f"{n2} is greater.")
else:
    print(f"{n3} is greater.")

