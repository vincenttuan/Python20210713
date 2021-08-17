import random

total = 100  # 我有 100 元
cash = total # 放到皮包
limit = int(cash/3)
amount = 0   #買到的禮物數量
while cash > 0:
    price = random.randint(1, 100)
    if(cash - price >= 0):
        cash = cash - price
        print('禮物 $ %d (買到) 剩下 $ %d' % (price, cash))
        amount = amount + 1
    else:
        print('禮物 $ %d (沒買到) 剩下 $ %d' % (price, cash))
        # 若還剩下 1/3 繼續買
        if cash >= limit:
            continue
        else:
            break;

# 統計：
# 總共買到 ? 份禮物, 禮物的平均價格 ?, 錢包還剩下 ?
gift_avg = (total - cash)/amount
print('總共買到 %d 份禮物, 禮物的平均價格 $%.1f, 錢包還剩下 $%d' % (amount, gift_avg, cash))




