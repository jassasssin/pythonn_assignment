class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative.")

# Example usage
account = Account(100)
print(account.get_balance())
account.set_balance(150)
print(account.get_balance())
