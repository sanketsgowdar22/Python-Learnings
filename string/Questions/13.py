# Remove duplicate characters from a string. 
str1 = input("Enter String :")
count = 0
list1 = []

for i in str1:
    if i in list1:
        list1.remove(i)
    else:
        list1.append(i)
print(list1)

    
