set1 = set()
n = int(input("enter the number of elements:"))
for i in range(n):
    ele = int(input(f"Enter elements {i}:"))
    set1.add(ele)
print(set1)

list1 = list(set1)
print(list1)

min = max = list1[0] 

for j in list1:
    if j > max:
        max = j
    if j < min:
        min = j
        
print(f"Min is {min}")
print(f"Max is {max}")




