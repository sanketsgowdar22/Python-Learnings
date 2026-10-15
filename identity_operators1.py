# a = 123
# b = 456
# c = a
# print(a is b)
# print(b is a)
# print(a is c)
# print(b is c)
# print(c is a)

a = 123
b = 123
c = a
print(a is b)
print(b is a)
print(a is not c)
print(b is c)
print(c is a)

print(id(a))
print(id(b))
print(id(c))
