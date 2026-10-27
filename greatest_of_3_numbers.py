#Finding the greatest among 3 numbers

num_1 = int(input("Enter number 1:"))
num_2 = int(input("Enter number 2:"))
num_3 = int(input("Enter number 3:"))

if(num_1 > num_2) and (num_1 > num_3):
    print(f"The {num_1} is greater")
elif(num_2 > num_1) and (num_2 > num_3):
    print(f"The {num_2} is greater")
else:
    print(f"The {num_3} is greater")
    
