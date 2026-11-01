# Write a program to find the absolute value of a number entered through the keyboard.

n = int(input("Enter the value for n:"))

if (n < 0):
    n = (n - (2 * n))
    print(f"The Absolute value is {n}")
else:
    print(f"The Absolute value is {n}")

