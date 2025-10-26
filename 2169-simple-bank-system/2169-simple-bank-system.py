from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        # Store the balances. self.balance[i] corresponds to account i+1.
        self.balance = balance
        # Store the total number of accounts for easy validation.
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Step 1: Validate both accounts.
        # Check if account numbers are within the valid range [1, n].
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False  # One or both accounts are invalid
        
        # Get 0-based indices
        index1 = account1 - 1
        index2 = account2 - 1

        # Step 2: Validate funds in the source account.
        if self.balance[index1] >= money:
            # Step 3: Perform the transaction
            self.balance[index1] -= money
            self.balance[index2] += money
            return True
        else:
            return False  # Insufficient funds

    def deposit(self, account: int, money: int) -> bool:
        # Step 1: Validate the account.
        if not (1 <= account <= self.n):
            return False  # Invalid account number
        
        # Step 2: Perform the deposit (always valid if account is valid)
        # Get 0-based index
        index = account - 1
        self.balance[index] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Step 1: Validate the account.
        if not (1 <= account <= self.n):
            return False  # Invalid account number

        # Get 0-based index
        index = account - 1
        
        # Step 2: Validate funds.
        if self.balance[index] >= money:
            # Step 3: Perform the withdrawal
            self.balance[index] -= money
            return True
        else:
            return False  # Insufficient funds


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)