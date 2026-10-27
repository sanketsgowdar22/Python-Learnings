string = input("Enter you word:")

if(string == string[::-1]):
    print(f"The given word {string} is a palindrome")
else:
    print(f"The given word {string} is not a palindrome")
