'''
迴圈 for-in、while
不知道要執行的次數
while 佈林判斷:
    程式區塊
'''
import random
while True:
    score = random.randint(0, 100)
    if score >= 60:
        print("pass score:", score)
    else:
        print("fail score:", score)
        break
