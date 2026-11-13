ls = [1,1,2,3,4,4,5,6,7,7,8,9,9,0,1,1]

new_ls = []

for i in ls:
    if i in new_ls:
        new_ls.remove(i)
    else:
        new_ls.append(i)
print(new_ls)
