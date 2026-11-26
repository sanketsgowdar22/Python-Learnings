numbers = [1,2,3,4,5]
sum = 0
for i in numbers:
    sum += i
print(sum)

from functools import reduce

result = reduce(lambda x,y: x+y,numbers)
print(result)
