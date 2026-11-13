# balance = 10000

def any_time_machine(bank,password,account_type,withdraw):
    print(f"Bank Name: {bank}")
    print(f"Password: {password}")
    print(f"Account Type: {account_type}")
    print(f"Withdraw: {withdraw}")
    balance = 1000
    # bal = balance - withdraw
    print(f"Balance: {balance - withdraw}")
any_time_machine("SBI",112233,"savings",5000)
