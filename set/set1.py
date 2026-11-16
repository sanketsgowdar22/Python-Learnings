set1 = {"Python",True,False,None,22,2.37,3+2j}

print(set1)
print(id(set1))
print(len(set1))
print(type(set1))

for ele in set1:
    print(hash(ele) ,"----->", ele)
    print(id(ele), "----->", ele)
    print("*"*10)
