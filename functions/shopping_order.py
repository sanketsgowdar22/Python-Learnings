def shopping_order(customer_name,*price):
    total_amount = sum(price)
    if total_amount > 5000:
        total_amount = total_amount - (total_amount * 0.10)
    print(f"The total amount of the customer {customer_name} is {total_amount}")
    print("*"*20)
    
shopping_order("Sanket",1000,1250,5400,400)
shopping_order("Chidu",1000,1000,1000,1000,1000)
