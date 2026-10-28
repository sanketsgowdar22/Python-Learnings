joining = int(input("Enter the joining year:"))
current = int(input("Enter the current year:"))

exp = (current - joining)

if(exp >= 10):
    print("Bonus 20%")
elif(exp >= 5 and exp <= 9):
    print("Bonus 10%")
elif(exp >= 2 and exp <= 4):
    print("Bonus 5%")
else:
    print("Work for more than 2 years")
