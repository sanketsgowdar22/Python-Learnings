day = int(input("Enter the Date:"))
month = int(input("Enter the Month:"))
year = int(input("Enter the Year:"))

if(day < 1 or day > 31):
    print("Invalid Day")
elif(month < 1 or month > 12):
    print("Invalid Month")
elif(month == 2):
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        if day <= 29:
            print(f"The date will be {day}-{month}-{year}")
        else:
            print("Invalid date") 
    else:
        if day <= 28:
            print(f"The date will be {day}-{month}-{year}")
        else:
            print("Invalid Date") 
elif(month == 4 or month == 6 or month == 9 or month == 11):
    if day <= 30:
        print(f"The date will be {day}-{month}-{year}")
    else:
        print("Invalid Date")
elif(day >= 31):
    print(f"The date will be {day}-{month}-{year}  and it is invalid date")
else:
    print("Invlaid Date")
