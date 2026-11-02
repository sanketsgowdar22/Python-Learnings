p_1 = int(input("Enter the amount of product 1:"))
p_2 = int(input("Enter the amount of product 2:"))
p_3 = int(input("Enter the amount of product 3:"))
p_4 = int(input("Enter the amount of product 4:"))

total = float(p_1+p_2+p_3+p_4)
print(f"The total amount of the products is {total}")

discount = (total / 1000)
# print(f"The discount percentage will be {discount}%")


if(total >= 10000):
    if(discount >= 10):
        print(f"The discount will be {discount}")
        total = total - (discount*100)
        print(f"The new total will be {total}")
    else:
        print(f"The discount is not applicable")
else:
    print(f"The total is less than 10000")


