order = input("Are you interested to order food(YES or NO):").lower()

if(order == "yes"):
    price = int(input("Enter the price:"))
    if (price >= 500):
        have_coupon = input("Do you have coupon(YES or NO):").lower()
        if(have_coupon == "yes"):
            price = price * 0.90
            print(f"Total amount is {price}")
        else:
            print(f"Total amount is {price}")
    else:
        print(f"The price is less than 500 pay full amount")
else:
    print("Order Cancelled")
