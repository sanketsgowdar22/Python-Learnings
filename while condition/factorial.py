num = int(input("Enter number:"))
i = 1
fact = 1

# while(num > 0):
#     fact = num * (num - 1)
#     num -= 1
#     print(f"Factorial of {temp} is {fact}")

while(i <= num):
    fact = fact * i
    i += 1
print(f"The Factorial {fact}")
