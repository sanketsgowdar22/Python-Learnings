# Write a program to check whether a number is between 1 and 100.

n = int(input("Enter number:"))

if(1 < n < 100):
# if(1 <= n <= 100): if we want the 1 and 100 to be printed then use this if loop
    print(f"{n} is between 1 to 100")
else:
    print(f"{n} is not between 1 to 100")
