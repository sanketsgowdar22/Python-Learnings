# Write a program to check whether a number lies outside the range 10 to 50.

n = int(input("Enter number:"))

if(10 < n < 50):
# if(1 <= n <= 100): if we want the 10 and 50 to be printed then use this if loop
    print(f"{n} is lies between 10 to 50")
else:
    print(f"{n} is not lies between 10 to 50")
