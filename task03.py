#ATM Withdrawal System

account = {
    "name": "Ali",
    "pin": 1234,
    "balance": 10000
}

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        return "Insufficient balance"

attempts = 0
logged_in = False

while attempts < 3:
    try:
        pin = int(input("Enter your PIN: "))
        
        if pin == account["pin"]:
            print("Login successful!")
            logged_in = True
            
            amount = float(input("Enter withdrawal amount: Rs. "))
            result = withdraw(account["balance"], amount)
            
            if result == "Insufficient balance":
                print("Insufficient balance")
            else:
                account["balance"] = result
                print("Withdrawal successful!")
                # Challenge: Show the remaining balance
                print(f"Remaining balance: Rs. {account['balance']}")
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts remaining: {3 - attempts}")
    except ValueError:
        print("Please enter a valid numeric PIN.")

if not logged_in:
    print("Account locked due to 3 incorrect PIN attempts.")