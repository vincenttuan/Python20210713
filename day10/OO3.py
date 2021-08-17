from day10 import Bank

# 轉帳
if __name__ == '__main__':
    account1 = Bank.Account('Vincent', 30000)
    account2 = Bank.Account('Anita', 50000)
    print(account1)
    print(account2)

    # 轉帳
    account1.transfer(25000, account2)
    print(account1)
    print(account2)
