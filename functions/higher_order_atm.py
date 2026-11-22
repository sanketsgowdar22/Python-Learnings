# Create an outer function atm() with an initial balance of ₹25,000.
# Inner functions:
# - PIN verification
# - Cash withdrawal
# - Balance- enquiry
# - Mini statement

def atm():
    balance = 25000
    set_pin = int(input("Set your pin:"))
    withdraw_amt = int(input("Enter the amount to withdraw:"))
    
    def pin_verification():
        print("*"*20)
        pin = int(input("Enter the PIN:"))
        
        if pin == set_pin:
            print("Auntheticated User")
            return True
        else:
            print("Invalid pin")
            return False
            
    def cash_withdrawal():
        print("*"*20)
        nonlocal balance
        
        if withdraw_amt <= 0:
            print("Enter valid amount to withdraw")
        elif withdraw_amt <= balance:
            balance = balance - withdraw_amt
        else:
            print("Insufficient Balance")

    
    def balance_enquiry():
        print("*"*20)
        
        print(f"Balance : {balance}")
                
    def mini_statement():
        print("*"*20)
        print("Mini Statement")
        print("Original Balance: 25000")
        print(f"Balance: {balance}")
        print(f"Withdraw amount : {withdraw_amt}")
        
    if pin_verification():
        cash_withdrawal()
        balance_enquiry()
        mini_statement()
    else:
        print("Invalid Transaction")
    
atm()        
