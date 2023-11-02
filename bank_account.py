class AccountDB:
    def __init__(self):
        self.account_database = []

    def insert(self, account):
        index = self.__search_private(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print(account.account_number, "Duplicated account; nothing to be inserted")

    def __search_private(self, account_num):
        for i, acc in enumerate(self.account_database):
            if acc.account_number == account_num:
                return i
        return -1

    def search_public(self, account_num):
        for acc in self.account_database:
            if acc.account_number == account_num:
                return acc
        return None

    def delete_account(self, account_num):
        account = self.search_public(account_num)
        if account:
            print("Deleting account:", account_num)
            self.account_database.remove(account)
        else:
            print(account_num, "invalid account number; nothing to be removed.")

    def __str__(self):
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s


class Account:
    def __init__(self, num, type, account_name, balance):
        self.account_number = num
        self.type = type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if self:
            print("Depositing", amount, "to", self.account_number)
            self.balance += amount
        else:
            print("Invalid account; no deposit action performed.")

    def withdraw(self, amount):
        if self:
            if self.balance >= amount:
                print("Withdrawing", amount, "from", self.account_number)
                self.balance -= amount
            else:
                print("Withdrawal amount", amount, "exceeds the balance of", self.balance, "for", self.account_number, "account.")
        else:
            print("Invalid account; no withdrawal action performed.")

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.type) + ',' + str(self.account_name) + ',' + str(self.balance) + '}'


if __name__ == "__main__":
    my_account_DB = AccountDB()

    account1 = Account("0000", "saving", "David Patterson", 1000)
    account2 = Account("0001", "checking", "John Hennessy", 2000)
    account3 = Account("0003", "saving", "Mark Hill", 3000)
    account4 = Account("0004", "saving", "David Wood", 4000)
    account5 = Account("0004", "saving", "David Wood", 4000)

    my_account_DB.insert(account1)
    my_account_DB.insert(account2)
    my_account_DB.insert(account3)
    my_account_DB.insert(account4)
    my_account_DB.insert(account5)

    print(my_account_DB)

    account = my_account_DB.search_public("0003")
    if account:
        account.deposit(50)
    else:
        print("Account not found.")

    print(my_account_DB)

    account = my_account_DB.search_public("0003")
    if account:
        account.withdraw(25)
    else:
        print("Account not found.")

    print(my_account_DB)

    my_account_DB.delete_account("0003")

    account = my_account_DB.search_public("0003")
    if account:
        account.deposit(50)
    else:
        print("Account not found.")

    account = my_account_DB.search_public("0001")
    if account:
        account.withdraw(6000)
    else:
        print("Account not found.")
    # account1 = Account("0000", "saving", "David Patterson", 1000)
    # account2 = Account("0001", "checking", "John Hennessy", 2000)
    # account3 = Account("0003", "saving", "Mark Hill", 3000)
    # account4 = Account("0004", "saving", "David Wood", 4000)
    # account5 = Account("0004", "saving", "David Wood", 4000)
    #
    # my_account_DB = AccountDB()
    # my_account_DB.insert(account1)
    # my_account_DB.insert(account2)
    # my_account_DB.insert(account3)
    # my_account_DB.insert(account4)
    # my_account_DB.insert(account5)
    # print(my_account_DB)
    #
    # account = my_account_DB.search_public("0003")
    # if account:
    #     account.deposit(50)
    # else:
    #     print("Account not found.")
    #
    # print(my_account_DB)
    #
    # account = my_account_DB.search_public("0003")
    # if account:
    #     account.withdraw(100)
    # else:
    #     print("Account not found.")
    #
    # print(my_account_DB)
    #
    # account = my_account_DB.search_public("0010")
    # if account:
    #     account.deposit(50)
    # else:
    #     print("Account not found.")
