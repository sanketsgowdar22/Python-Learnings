# Find the largest word in a sentence. 

str1 = input("Enter the sentence:")
words = str1.split()

largest = words[0]

for i in words:
    if len(i) > len(largest):
        largest = i
print(largest)
