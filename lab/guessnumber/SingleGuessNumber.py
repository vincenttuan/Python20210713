'''
由系統產生 1~99 之間的亂數
假設 ans = 77
      min ~  max
=> 請在 0 ~ 100 之間猜一個數字
使用者猜 50
=> 請在 50 ~ 100 之間猜一個數字
使用者猜 90
=> 請在 50 ~ 90 之間猜一個數字
...
使用者猜 77
答對了 !

ps:
最多猜 7 次, 若超過則程式自動(while)結束
'''
import random

ans = random.randint(1, 99)
min, max = 0, 100
max_amount = 7
cur_amount = 0

while True:
    # 使用次數 +1
    cur_amount = cur_amount + 1
    if cur_amount > max_amount:
        print('次數用完，程式結束。答案：%d' % ans)
        break

    # User 猜 (最多猜 7 次)
    guess = input('( %d/%d )請在 %d ~ %d 之間猜一個數字: ' % (cur_amount, max_amount, min, max))
    guess = int(guess)  # 將字串轉數字

    # 驗證範圍 ?
    if(guess <= min or guess >= max):
        print('範圍錯誤, 請重新輸入 !')
        continue

    # 判斷是否猜對 ?
    if guess < ans:
        min = guess
    elif guess > ans:
        max = guess
    else:
        print('恭喜猜對了 !')
        break # while 回圈結束




