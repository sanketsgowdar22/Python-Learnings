# Check whether given phone number is valid or invalid
    
def phone_number(number):
    if len(number) == 10 and number.isdigit():
        num = str(number)
        if num[0] in "6789":
            return"Valid Phone Number"
        else:
            return"Invalid Phone Number"
    else:
        return"Enter 10 digits to validate"
        
number = input("Enter a phone number:")
print(phone_number(number))
