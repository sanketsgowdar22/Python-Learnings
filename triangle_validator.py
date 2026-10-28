a = int(input("Enter the angle of a:"))
b = int(input("Enter the angle of b:"))
c = int(input("Enter the angle of c:"))

if(a >= 1) and (b >= 1) and ( c >= 1) and (a + b + c == 180): 
    if(a == b == c):
        print("Equilateral Triangle")
    elif(a == b) or (b == c) or (a == c):
        print("Isoscale Trianle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Triangle")
