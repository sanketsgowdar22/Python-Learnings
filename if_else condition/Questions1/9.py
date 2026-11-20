# If the three sides of a triangle are entered through the keyboard, 
# Write a program to check whether the triangle is isosceles, equilateral, scalene or right angled triangle.

s1 = int(input("Enter side s1:"))
s2 = int(input("Enter side s2:"))
s3 = int(input("Enter side s3:"))

a1 = int(input("Enter angle a1:"))
a2 = int(input("Enter angle a2:"))
a3 = int(input("Enter angle a3:"))

if(s1 == s2 == s3):
    print("Equilateral Triangle")
elif(s1 == s2) or (s2 == s3) or (s3 == s1):
    print("Isoscale Triangle")
else:
    print("Scalene Triangle")

if(a1+a2+a3 == 180): 
    if(a1 == 90) or (a2 == 90) or (a3 == 90):
        print("Right Angled Triangle")
    else:
        print("Not a Right Angled Triangle")
else:
    print("Not a Triangle")
    
