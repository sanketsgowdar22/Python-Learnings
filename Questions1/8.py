# If the three sides of a triangle are entered through the keyboard, 
# Write a program to check whether the triangle is valid or not. 
# The triangle is valid if the sum of two sides is greater than the largest of the three sides.

side_1 = int(input("Enter the value of side_1:"))
side_2 = int(input("Enter the value of side_2:"))
side_3 = int(input("Enter the value of side_3:"))

if ((side_1 + side_2) <= side_3):
    print("Invalid Triangle")
elif((side_1 + side_3) <= side_2):
    print("Invalid Triangle")
elif((side_3 + side_2) <= side_1):
    print("Invalid Triangle")
else:
    print("Valid Triangle")
