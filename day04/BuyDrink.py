# 買飲料的程式
# 飲料一瓶 10 元
# 買二送一
# 試問：若有 110 元，最多可以買幾瓶飲料 ?

if __name__ == '__main__':
    price = 10     # 飲料一瓶 10 元
    balance = 100  # 皮包內有 100 元

    amount = int(balance/price)
    bonus = int(amount/2)
    amount = amount + bonus
    print(amount)
