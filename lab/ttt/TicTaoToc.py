ttt = [
    ['O', 'O', 'X'],
    ['X', 'O', ' '],
    ['X', ' ', 'X']
]

for row in ttt:
    print(row)

n = int(input('請輸入位置 0~8: '))
# 如何讓「O」贏 ?
x = n // 3  # 橫(列)
y = n % 3   # 縱(行)
ttt[x][y] = 'O'

for row in ttt:
    print(row)

