# Count vowels and consonants in a string

str = input("Enter the string:")
vowel = 0
consonants = 0
i = 0

# while (len(str) > i):
#     if("aeiouAEIOU" in str):
#         vowel += 1
#     else:
#         consonants += 1
#     i += 1
# print(f"Total vowels {vowel}")
# print(f"Total consonants {consonants}")   

for i in str:
    if i in "aeiouAEIOU":
        vowel += 1
    else:
        consonants += 1
print(f"Total vowels {vowel}")
print(f"Total vowels {consonants}")
