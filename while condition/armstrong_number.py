# num = int(input("Enter the number:"))
# l = 0
# sum = 0

# while(num > 0):
#     i = num % 10
#     l += 1
#     num = num // 10
# print(f"The length of n is {length}")
#     sum = i ** l
    

n = int(input("Enter number:"))
temp = n
power = len(str(n))
total = 0

while(temp > 0):
    rem = temp % 10
    total = total + (rem ** power)
    temp //= 10
if (n == total):
    print("Armstrong")
else:
    print("Not Armstrong")
