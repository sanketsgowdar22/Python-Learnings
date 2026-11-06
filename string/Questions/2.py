# Check whether a string is a palindrome

str = input("Enter the string:")
rev = str[::-1]

if str == rev:
    print(f"The given {str} is  palindrome")
else:
    print(f"the given {str} is not a plaindrome")
