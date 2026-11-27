# Find the frequency of each word in a sentence. 
str1 = input("Enter the sentence:")
words = str1.split()

for i in words:
    count = words.count(i)
    print(f"The frequency of the word {i}: {count}")
