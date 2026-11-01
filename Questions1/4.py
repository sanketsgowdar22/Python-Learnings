# Write a program to check whether a triangle is valid or not , 
# When the three angles of the triangle are entered through the keyboard. 
# A triangle is valid if the sum of all the three angles is equal to 180 degrees.

angle_1 = int(input("Enter the angle_1:"))
angle_2 = int(input("Enter the angle_2:"))
angle_3 = int(input("Enter the angle_3:"))

if ((angle_1 + angle_2 + angle_3) == 180):
    print("Triangle")
else:
    print("Invalid Triangle")
