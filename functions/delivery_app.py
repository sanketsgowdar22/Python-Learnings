# def delivery(price,distance,charge=0):
#     if price > 500:
#         return f"Got a free delivery on price above {price}"
#     elif price < 500 and distance < 5:
#         return f"Got a free delivery because distance {distance} is less than 5km"
#     else:
#         return f"Total price for the item will be {price+charge}"
    
# price=int(input("Enter the price:"))
# distance=int(input("Enter the distance:"))
# charge=int(input("Enter the charge:"))
# print(delivery(price,distance,charge))

price=int(input("Enter the price:"))
distance=int(input("Enter the distance:"))
charge=int(input("Enter the charge:"))
amount = 500
travel = 5

def delivery(price,distance,charge=0):
    return f"The price will be {price+charge}"

if amount < price:
    print(delivery(price,distance))
    # print(f"Got a free delivery on price above {price}")
elif price < amount and  distance < travel :
    print(delivery(price,distance))
    # print(f"Got a free delivery because distance {distance} is less than 5km")
else:
    print(delivery(price,distance,charge))
    # print(f"Total price for the item will be {price+charge}")


