account_database = []


class AccountDB:
    def __init__(self):
        self.account_database = []

    def insert(self, account):
        index = self.__search_private(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print(account, "Duplicated account; nothing to be insert")

    def __search_private(self, account_num):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == account_num:
                return i  # index
        return -1

    def search_public(self, account_num):
        for account in self.account_database:
            if account.account_number == account_num:
                return account  # acocunt
        return None

    # def create_account(num, type, name, init_balance):
    #     index = search_account_db(num)
    #     if index == -1:
    #         account = {}
    #         account["account_number"] = num
    #         account["type"] = type
    #         account["account_name"] = name
    #         account["balance"] = init_balance
    #         account_database.append(account)
    #     else:
    #         print("Account", num, "already exists")

    def create_account(self, account_num, type, name, init_balance):
        # index = search_account_db(num)
        search_account = self.__search_private(account_num)
        if search_account == -1:
            account = {"account_number": account_num, "type": type,
                       "account_name": name, "balance": init_balance}
            self.account_database.append(account)
        else:
            print("Account", account_num, "already exists")

    # def delete_account(num):
    #     index = search_account_db(num)
    #     if index != -1:
    #         print("Deleting account:",
    #               account_database[index]["account_number"])
    #         del account_database[index]
    #     else:
    #         print(num, "invalid account number; nothing to be deleted.")

    def delete_account(self, account_num):
        search_account = self.__search_private(account_num)
        if search_account != 1:
            print("Deleting account:", account_num)
            del account_database[i]
        else:
            print(account_num, "invalid account number; nothing to be deleted.")

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

    # def deposit(account_num, amount):
    #     index = search_account_db(account_num)
    #     if index != -1:
    #         print("Depositing", amount, "to",
    #               account_database[index]["account_number"])
    #         account_database[index]["balance"] += amount
    #     else:
    #         print(account_num,
    #               "invalid account number; no deposit action performed.")

    # def deposit(self, amount):
    #     index = self.__search_private(self.account_number)
    #     if index != -1:
    #         print("Depositing", amount, "to", self.account_number)
    #         self.balance += amount
    #     else:
    #         print(self.account_number, "invalid account number; no deposit action performed.")

    def deposit(self, amount):
        index = AccountDB().search_public(self.account_number)
        if index is not None:
            self.balance += amount
        else:
            print(self.account_number, "invalid account number; no deposit action performed.")


    # def deposit(self, amount):
    #     index = AccountDB().search_public(self.account_number)
    #     if index is not None:
    #         self.balance += amount
    #     else:
    #         print(self.account_number, "invalid account number; no deposit action performed.")

    # def withdraw(account_num, amount):
    #     index = search_account_db(account_num)
    #     if index != -1:
    #         if account_database[index]["balance"] >= amount:
    #             print("Withdrawing", amount, "from",
    #                   account_database[index]["account_number"])
    #             account_database[index]["balance"] -= amount
    #         else:
    #             print("withdrawal amount", amount, "exceeds the balance of",
    #                   account_database[index]["balance"], "for", account_num,
    #                   "account.")
    #     else:
    #         print(account_num,
    #               "invalid account number; no withdrawal action performed.")

    def withdraw(self, amount):
        index = AccountDB().search_public(self.account_number)
        if index is not None:
            if self.balance >= amount:
                print("Withdrawing", amount, "from", account_database[index])
                self.balance -= amount
        else:
            print("withdrawal amount", amount, "exceeds the balance of", index)

    def show_account(self, account_num):
        index = AccountDB().search_public(self.account_number)
        if index is not None:
            print("Showing details for", account_num)
            print(index)
        else:
            print(account_num, "invalid account number; nothing to be shown for.")

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.type) + ',' + str(self.account_name) + ',' + str(self.balance) + '}'



# create_account("0000", "saving", "David Patterson", 1000)
# create_account("0001", "checking", "John Hennessy", 2000)
# create_account("0003", "saving", "Mark Hill", 3000)
# create_account("0004", "saving", "David Wood", 4000)
# create_account("0004", "saving", "David Wood", 4000)
# print(account_database)
# show_account('0003')
# deposit('0003', 50)
# show_account('0003')
# withdraw('0003', 25)
# show_account('0003')
# delete_account('0003')
# show_account('0003')
# deposit('0003', 50)
# withdraw('0001', 6000)
account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
my_account_DB = AccountDB()
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)
my_account_DB.insert(account4)
my_account_DB.insert(account5)
print(my_account_DB)
print()
my_account_DB.search_public("0003").deposit(50)
print(my_account_DB)
my_account_DB.search_public("0003").withdraw(100)
print(my_account_DB)
my_account_DB.search_public("0010").deposit(50)
print(my_account_DB)

