'''
由系統產生 1~99 之間的亂數
User 與 PC 對戰
'''
import random
import sys

ans = random.randint(1, 99)
min, max = 0, 100

while True:

    # User 猜
    guess = input('User 請在 %d ~ %d 之間猜一個數字: ' % (min, max))
    guess = int(guess)  # 將字串轉數字

    # 驗證範圍 ?
    if(guess <= min or guess >= max):
        print('User 輸入的範圍錯誤 !')
    else:
        # 判斷 User 是否猜對 ?
        if guess < ans:
            min = guess
        elif guess > ans:
            max = guess
        else:
            print('恭喜 User 猜對了 !')
            break  # while 回圈結束

    # 按下 Enter 讓電腦猜
    print('按下 Enter 讓電腦猜 ...')
    sys.stdin.read(1)

    # 電腦(PC)猜
    # 例如：40 ~ 60 -> 41 ~ 59
    guess = random.randint(min+1, max-1)
    print('電腦(PC)在 %d ~ %d 之間猜一個數字: %d' % (min, max, guess))

    # 判斷 電腦(PC) 是否猜對 ?
    if guess < ans:
        min = guess
    elif guess > ans:
        max = guess
    else:
        print('恭喜 電腦(PC) 猜對了 !')
        break  # while 回圈結束



