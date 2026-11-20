# Given the length and breadth of a rectangle, 
# Write a program to find whether the area of the rectangle is greater than its perimeter.
# For example, the area of the rectangle with length = 5 and breadth = 4 is greater than its perimeter.

l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle:"))

area = l * b
perimeter = 2 * (l + b)

if(area > perimeter):
    print("Area is greater")
else:
    print("Perimeter is greater")
