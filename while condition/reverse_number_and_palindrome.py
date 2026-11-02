num = int(input("Enter number:"))
temp = num
rev = 0

while(num > 0):
    i = num % 10
    rev = rev * 10 + i
    num //= 10
else:
    print(f"Reverse of the number:{rev}")
    
if(temp == rev):
    print(f"The given {temp} is palindrome")
else:
    print("Not a Plaindrome")

