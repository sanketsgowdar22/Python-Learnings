n = int(input("Enter number:"))
length = 0

while(n > 0):
    i = n % 10
    length += 1
    n = n // 10
else:
    print(f"The length of n is {length}")
