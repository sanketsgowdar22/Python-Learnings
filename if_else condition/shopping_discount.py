amount = int(input("Enter the total amount:"))

if(amount > 5000):
    if(amount >= 8000) and (amount <= 12000):
        discount = 20
        print(f"The discount is {discount}%")
        amount = amount - (amount * 20 / 100)
        # amount = amount * 0.80
        print(f"Total payable amount is {amount}")
    elif(amount >= 5001) and (amount <= 7999):
        discount = 12
        print(f"The discount is {discount}%")
        amount = amount - (amount * 12 / 100)
        # amount = amount * 0.88
        print(f"Total payable amount is {amount}")
    else:
        print(f"The {amount} is not available for discount")
else:
    print(f"Thank you for Shopping")
