# Find the power of number

# def power(b,n):
#     if n == 0:
#         return 1
#     return b ** n
# b = int(input("Enter the base number:"))
# n = int(input("Enter the power number:"))
# print(f"Power of the base {b} with power {n} : {power(b,n)}")

def power(b,n):
    if n == 0:
        return 1
    return b * power(b,n-1)
b = int(input("Enter the base number:"))
n = int(input("Enter the power number:"))
print(f"Power of the base {b} with power {n} : {power(b,n)}")
