num = int(input("Enter your number:"))

if (num >= 1) and (num <= 9):
    print(f"The given {num} is single digit")
elif(num >= 10) and (num <= 99):
    print(f"The given {num} is Double digit")
elif(num >= 100) and (num <= 999):
    print(f"The given {num} is Thrible digit")
else:
    print(f"the given {num} is either of them")

if (num < 10):
    print(f"The {num} is single digit")
elif(num < 100):
    print(f"The {num} is double digit")
elif(num < 100):
    print(f"The {num} is thirble digit")
else:
    print(f"The {num} is either of them")
