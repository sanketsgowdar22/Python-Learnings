# Write a program to check whether a number is positive, negative, or zero.

n = int(input("Enter the number:"))

if(n == 0):
    print(f"The entered number {n} is zero.")
elif(n < 0):
    print(f"The entered number {n} is negative.")
else:
    print(f"The entered number {n} is positive.")
