n = int(input("Enter your number:"))

if (n % 2 == 0): #when the remainder is 0
    print(f"The given {n} is even")
else:
    print(f"The given {n} is odd")
    
if (n % 2 == 1): #when the remainder is 1
    print(f"The given {n} is odd")
else:
    print(f"The given {n} is even")
