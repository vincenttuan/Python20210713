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


def keepGoing():
    for row in ttt:
        for value in row:
            if value == ' ':
                return True
    return False

def theWinnerIs():
    if ttt[0][0] + ttt[0][1] + ttt[0][2] == 'OOO' or \
       ttt[1][0] + ttt[1][1] + ttt[1][2] == 'OOO' or \
       ttt[2][0] + ttt[2][1] + ttt[2][2] == 'OOO' or \
       ttt[0][0] + ttt[1][0] + ttt[2][0] == 'OOO' or \
       ttt[0][1] + ttt[1][1] + ttt[2][1] == 'OOO' or \
       ttt[0][2] + ttt[1][2] + ttt[2][2] == 'OOO' or \
       ttt[0][0] + ttt[1][1] + ttt[2][2] == 'OOO' or \
       ttt[0][2] + ttt[1][1] + ttt[2][0] == 'OOO' :
        print('使用者贏')
        return True

    if ttt[0][0] + ttt[0][1] + ttt[0][2] == 'XXX' or \
       ttt[1][0] + ttt[1][1] + ttt[1][2] == 'XXX' or \
       ttt[2][0] + ttt[2][1] + ttt[2][2] == 'XXX' or \
       ttt[0][0] + ttt[1][0] + ttt[2][0] == 'XXX' or \
       ttt[0][1] + ttt[1][1] + ttt[2][1] == 'XXX' or \
       ttt[0][2] + ttt[1][2] + ttt[2][2] == 'XXX' or \
       ttt[0][0] + ttt[1][1] + ttt[2][2] == 'XXX' or \
       ttt[0][2] + ttt[1][1] + ttt[2][0] == 'XXX' :
        print('電腦贏')
        return True

    return False

def play():
    # 使用者玩「O」
    if not keepGoing():  # 是否有空間可以繼續玩 ?
        return False
    n = int(input('請輸入位置（0~8）：'))

    if n == -1:
        return False  # 離開

    ttt[n // 3][n % 3] = 'O'
    printTTT()  # 印出盤面
    if theWinnerIs():  # 判斷是否有贏家
        return False
    #-------------------------------------------
    # 電腦玩「X」
    if not keepGoing():  # 是否有空間可以繼續玩 ?
        return False
    print('電腦計算中...')
    t.sleep(2)
    while True:
        n = r.randint(0, 8)
        if ttt[n // 3][n % 3] == ' ':
            ttt[n // 3][n % 3] = 'X'
            break

    printTTT()  # 印出盤面
    if theWinnerIs():  # 判斷是否有贏家
        return False

    return True  # 繼續玩

if __name__ == '__main__':
    printTTT()  # 印出盤面
    while play():
        pass

