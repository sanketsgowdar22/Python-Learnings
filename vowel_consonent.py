char = input("Enter the Character:")

if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
    print(f"The given character {char} is a Vowel")
else:
    print(f"The given character {char} is a Consonenet")


if(char in "aeiouAEIOU"):
    print(f"The given character {char} is a Vowel")
else:
    print(f"The given character {char} is a Consonenet")
    
