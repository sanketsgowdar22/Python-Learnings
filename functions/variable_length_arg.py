def bill(*price):
    return f"Total bill {sum(price)}"
print(bill(10,20,30,40,50))
