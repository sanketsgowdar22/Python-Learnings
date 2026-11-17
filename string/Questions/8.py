# Count words in a sentence. 
sen = input("Enter sentence:")
strip = sen.replace(" ","")
count = 0

for chr in strip:
    count += 1
print(count)
