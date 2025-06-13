import sys
from bank_account import BankAccount

def main():
    account = BankAccount(250)  # Example creates a bank account starting from 100
    if len(sys.argv) < 2: #remember 0 is script name, 1 is first argument... so if <2 then...
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':') #Gets the first command-line argument (like "deposit:50"). 

#Splits it at the colon (:) into:
#command = "deposit"
#params = ["50"]
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        print(account.display_balance())
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

