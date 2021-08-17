import random as r
# 骰子遊戲
# 有三顆骰子, 點數組合
# 3, 4, 5, 6, 7, 8, 9, 10 <- 猜小
# 11,12,13,14,15,16,17,18 <- 猜大

if __name__ == '__main__':
    dice_log = []  # 用來記錄每一次骰子的點數(dice_number)
    balance = 100  # 現金餘額
    while True:
        # 判斷現金餘額
        if balance <= 0:
            print("現金餘額 $%d 不足，請離場～" % balance)
            break;
        guess = int(input('現金餘額: $%d , 猜大小, 大=1, 小=2, 離開=0, 看log=9: ' % balance))

        # 判斷 guess
        if guess == 0:
            print('離開')
            break;

        if guess == 9:
            print('看 dice_log:', dice_log)
            continue;

        # 下注:
        while True:
            bet = int(input('請下注 (金額不可超過 $%d): ' % balance))
            if bet > balance:
                print('下注金額: $%d 目前現金餘額: $%d' % (bet, balance))
                continue
            elif bet <= 0:
                print('下注金額不正確')
                continue
            else:
                break;

        # 擲骰子
        dice_number = r.randint(1, 6) + r.randint(1, 6) + r.randint(1, 6)
        # log 紀錄
        dice_log.append(dice_number)

        if guess == 1:  # 猜大
            if(dice_number > 10):
                print("骰子點數: %d 猜大猜對了" % dice_number)
                balance = balance + bet
            else:
                print("骰子點數: %d 猜大猜錯了" % dice_number)
                balance = balance - bet
        elif guess == 2: # 猜小
            if (dice_number <= 10):
                print("骰子點數: %d 猜小猜對了" % dice_number)
                balance = balance + bet
            else:
                print("骰子點數: %d 猜小猜錯了" % dice_number)
                balance = balance - bet
        else:
            print('資料不正確，請重新輸入')
            continue

    # 顯示 log
    print(dice_log)
