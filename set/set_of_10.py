# n = int(input("Enter the number of elements in the set:"))
set1 = {1,2,3,4,5,6,7,8,9,10}
set2=set()
set3 = set()

print(set1)
for i in set1:
    if i % 2 == 0:
        set2.add(i)
        # print(f"{i} is even")
    else:
        set3.add(i)
        # print(f"{i} is odd")
print(set2)
print(set3)


