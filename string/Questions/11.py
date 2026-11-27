# Check whether two strings are anagrams.
str_1 = input("Enter String 1:")
str_2 = input("Enter String 2:")

if len(str_1) == len(str_2):
    for i in str_1:
        if i in str_2:
            break
    print("Given Strings are Anagrams")
else:
    print("Given Strings are not Anagrams")
    
print("*"*30)

if len(str_1) == len(str_2):
    for i in str_1:
        if str_1.count(i)==str_2.count(i):
            print("Given Strings are Anagrams")
            break
    else:
        print("Given Strings are not Anagrams")
else:
    print("Given Strings are not Anagrams")
