num  = int(input("Enter number:"))
sum = 0

while (num > 0):
    i = num % 10
    sum += i
    num //= 10
print(f"Sum of number:{sum}")
