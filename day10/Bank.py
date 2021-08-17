class Account:
    name      = ''  # 公有屬性
    __balance = 0   # 私有屬性

    def __init__(self, name, balance) -> None:
        self.name = name
        if balance > 0:
            self.__balance = balance

    def transfer(self, amount, acct):  # 轉帳
        if self.withdraw(amount) == True:
            acct.saving(amount)

    def saving(self, amount):  # 存款
        if amount > 0:
            self.__balance = self.__balance + amount
            print('存款 $%d 成功' % amount)
            return True
        else:
            print('存款 $%d 失敗' % amount)
            return False


    def withdraw(self, amount):  # 提款
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance - amount
            print('提款 $%d 成功' % amount)
            return True
        else:
            print('提款 $%d 失敗' % amount)
            return False


    def printBalance(self):
        print('帳戶餘額 $%d' % self.__balance)

    def __str__(self) -> str:
        return self.name + " $" + str(self.__balance)

