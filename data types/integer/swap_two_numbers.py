# Using third variable
print("Using third variable")
a = int(input("Enter the value of A:"))
b = int(input("Enter the value of B:"))

c = a
a = b
b = c

print(a)
print(b)

# Without using the third variable
print("Without using third variable")
a = int(input("Enter the value of A:"))
b = int(input("Enter the value of B:"))

a,b = b, a

print(a)
print(b)
