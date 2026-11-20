# Write a program that takes a number (1–3) and performs:
# •	1 → Addition
# •	2 → Subtraction
# •	3 → Multiplication

n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))

choice = int(input("Enter your choice:"))

if(choice == 1):
    addition = n1 + n2
    print(f"The addition of {n1} and {n2} is {addition}")
elif(choice == 2):
    subtraction = n1 - n2
    print(f"The substraction of {n1} and {n2} is {subtraction}")
elif(choice == 3):
    multiplication = n1 * n2
    print(f"The multiplication of {n1} and {n2} is {multiplication}")
else:
    print("Invalid Choice")





