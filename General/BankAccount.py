class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance is {self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount:.2f}. New balance is {self.balance:.2f}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance: {self.balance:.2f}")

def main():
    print("Welcome to the Simple Banking System!")
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder's name: ")
    
    account = BankAccount(account_number, account_holder)
    
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            account.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the Simple Banking System!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
