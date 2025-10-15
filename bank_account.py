class BankAccount:

    def __init__(self, owner_name):
        self.current_balance = 0
        self.owner_name = owner_name

    def deposit(self, balance):
        if self.current_balance == 0 and balance > 0:
            self.current_balance = balance
            print(
                f"Depositing for the first time. Balance: {balance} tk added successfully."
            )
        else:
            self.current_balance = self.current_balance + balance
            print(f"Balance deposit of {balance} tk added successfully.")

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.current_balance:
            print(f"Insufficient Balance! Current Balance: {self.current_balance} tk")
        else:
            self.current_balance = self.current_balance - withdrawal_amount
            print(f"Balance withdrawal of {withdrawal_amount} tk successful.")

    def display(self):
        print(f"Account Holder name: {self.owner_name}")
        print(f"Current Balance: {self.current_balance} tk")


owner = BankAccount("Sakib")
owner.display()  # tk 0 cz deposit not done
owner.deposit(500)  # depositing for the first time
owner.display()  # tk 1000
owner.withdraw(1000)
owner.deposit(1000)
owner.display()
owner.withdraw(200)
owner.display()
