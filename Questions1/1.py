# Any integer is input through the keyboard. 
# Write a program to find out whether it is an odd number or even number.

n = int(input("Enter the number:"))

if (n % 2 == 0):
    print(f"The given number {n} is even.")
else:
    print(f"The given number {n} is odd")
