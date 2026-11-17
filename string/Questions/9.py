# Find the first non-repeated character. 

string = input("Enter your string:")

for char in string:
    if char not in string[:string.index(char)]:
        if string.count(char) == 1:
            print("The first non-repeated characted is",char)
            break # break will stop the loop here itself , no iterations after this
