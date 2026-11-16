def resturant_bill(name,*food_price):
    total = sum(food_price)
    print(f"The total amount of the dinner of {name} is {total}")
    print("_"*30)
    
resturant_bill("Sanket",100,200,300,170,350)
resturant_bill("Rakshith",250,25,50)
