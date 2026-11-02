num = int(input("Enter number:"))
i = 1

while(i <= num % 2):
    # print(i)
    i += 1
    if(num % i == 0):
        print(f"The {num} is not prime number.")
    else:
        print(f"The {num} is a prime number")
else:
    print("Completed")
