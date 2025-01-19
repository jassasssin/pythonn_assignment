class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

# Example usage
account = BankAccount(100)
print(account.get_balance())
account.set_balance(150)
print(account.get_balance())
