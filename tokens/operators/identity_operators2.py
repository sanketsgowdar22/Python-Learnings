a = [10,20,30]
b = [10,20,31]
c = a

print(a is b)
print(b is a)
print(a is c)
print(b is c)
print(c is a)

print(id(a))
print(id(b))
print(id(c))
