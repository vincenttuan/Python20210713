from day10 import Bank

# 存款/提款
if __name__ == '__main__':
    account = Bank.Account('Vincent', 30000)
    account.printBalance()
    account.saving(10000)
    account.withdraw(6000)
    account.withdraw(5000)
    account.saving(-2000)
