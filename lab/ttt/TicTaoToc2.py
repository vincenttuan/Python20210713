import random as r
import time as t

ttt = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def printTTT():
    for row in ttt:
        print(row)

def play():
    printTTT()
    # 使用者玩「O」
    n = int(input('請輸入位置（0~8）：'))

    if n == -1:
        return False  # 離開

    ttt[n // 3][n % 3] = 'O'

    # 電腦玩「X」
    print('電腦計算中...')
    t.sleep(2)
    while True:
        n = r.randint(0, 8)
        if ttt[n // 3][n % 3] == ' ':
            ttt[n // 3][n % 3] = 'X'
            break

    return True  # 繼續玩

if __name__ == '__main__':
    while play():
        pass

