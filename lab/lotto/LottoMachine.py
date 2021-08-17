'''
Lotto 機器
可以提供重複或不重複的彩球
例如 : 輸入1 -> 開獎今彩539: 1~39 之間取不重複的 5 個彩球
      輸入2 -> 開獎四星彩 : 4 個 0~9 可以重複的數字
      輸入3 -> 開獎6/49大樂透 : 1~49 之間取不重複的 6 個彩球 + 1 個特別號
              Ex: 大樂透：27 36 42 40 29 05 特別號：35
      輸入0 -> Exit
'''
import random
import sys

def menu():
    print('------------')
    print('1. 今彩539')
    print('2. 四星彩')
    print('3. 6/49大樂透')
    print('0. Exit')
    print('------------')

def userChoice():
    choice = int(input('請選擇: '))
    return choice

def lotto539():
    # 請同學練習看看 ...
    # 1~39 之間取不重複的 5 個彩球
    # 提示: set(), len(), while
    lotto = set()
    while len(lotto) < 5:
        lotto.add(random.randint(1, 39))

    print('539:', lotto)


def lotto4Stars():
    lotto = []
    for x in range(4):
        lotto.append(random.randint(0, 9))
    print('四星彩:', lotto)

def lottoBig():
    n = 7
    lotto = set()
    while len(lotto) < n:
        lotto.add(random.randint(1, 49))

    lotto = tuple(lotto)
    print('大樂透所有獎號:', lotto)
    print('大樂透:', lotto[0:n-1], "特別號:", lotto[n-1])

if __name__ == '__main__':
    while True:
        # Lotto 開獎 menu()
        menu()
        # User 選擇
        choice = userChoice()
        # 判斷選擇
        if choice == 1:
            lotto539()
        elif choice == 2:
            lotto4Stars()
        elif choice == 3:
            lottoBig()
        elif choice == 0:
            print('離開程式')
            break
        else:
            print('輸入錯誤，請重新輸入 !')
            continue

        print('Enter...')
        sys.stdin.read(1)