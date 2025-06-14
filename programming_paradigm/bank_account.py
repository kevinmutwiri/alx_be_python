class BankAccount:
    def __init__(self, initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self._account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._account_balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance}")
