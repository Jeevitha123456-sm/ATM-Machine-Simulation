class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin
    
    def check_balance(self):
        print(f"Your account balance is: ${self.balance:.2f}")
        self.transaction_history.append("Checked balance")
    
    def withdraw_cash(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}")
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
    
    def deposit_cash(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Successfully deposited ${amount:.2f}")
        self.transaction_history.append(f"Deposited ${amount:.2f}")
    
    def change_pin(self):
        new_pin = input("Enter new PIN: ")
        self.pin = new_pin
        print("PIN successfully changed!")
        self.transaction_history.append("Changed PIN")
    
    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


def main():
    user_atm = ATM(pin="1234", balance=1000)
    
    if not user_atm.verify_pin():
        print("Incorrect PIN. Exiting...")
        return
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            user_atm.check_balance()
        elif choice == "2":
            user_atm.withdraw_cash()
        elif choice == "3":
            user_atm.deposit_cash()
        elif choice == "4":
            user_atm.change_pin()
        elif choice == "5":
            user_atm.show_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
