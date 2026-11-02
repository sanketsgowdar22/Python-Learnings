n = int(input("Enter number:"))
temp = n
i = 1
total = 0

while(i < temp):
    if(temp % i == 0):
        print(i)
        total = total + i
    i += 1   
if(total == n):
    print("Perfect Number")
else:
    print("Not Perfect Number")
