n = int(input("Enter the number of rows:"))

# 1st way
for i in range(n,0,-1):
    for j in range(i+1,1,-1):
        print(n , end = " ")
    n -= 1
    print()

# 2nd way
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i , end = " ")
    print()
    
# 3rd way
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(i , end = " ")
    print()

