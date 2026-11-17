# Find duplicate characters in a string. 
string = input("Enter the string:")

for char in string:
    if char not in string[:string.index(char)]:
        if string.count(char) >= 2:
            print("Duplicated characters in a string",char)
