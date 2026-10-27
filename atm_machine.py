balance = int(input("Enter the Balance Amount:"))
withdraw = int(input("Enter the Withdraw Amount:"))

if(balance > withdraw):
    balance = balance - withdraw
    print(f"Amount of {withdraw} is withdrawned")
    print(f"The remaining balance is {balance}")
else:
    print(f"You dont have sufficient {balance}")
