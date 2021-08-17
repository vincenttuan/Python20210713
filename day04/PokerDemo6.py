# 10點半對戰
# 今天你有 100 元
# 可以自由下注
# 下注金額不可以超過 balance 也不可以是負值
import day04.PokerDemo5 as poker

if __name__ == '__main__':
    balance = 100
    while True:
        print('balance:', balance)
        if balance == 0:
            print('你沒錢了，請離開遊戲...')
            break;

        bet = int(input('請下注(0:離開): '))

        if bet == 0:
            print('離開遊戲...')
            break;

        # 下注金額不可以超過 balance 也不可以是負值
        if bet < 0 or bet > balance:
            print('下注金額不可以超過 %d 也不可以是負值, 請重新下注' % balance)
            continue

        result = poker.playGame()
        #print(result)
        balance = balance + (result * bet)
        #print(balance)
