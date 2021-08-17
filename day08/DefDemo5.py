# 每次呼叫可以 +10 分
# 方法裡的 global
def addTen():
    global score
    score = score + 10


if __name__ == '__main__':
    score = 50
    print('score =', score)  # 50
    addTen()
    print('score =', score)  # 60
    addTen()
    addTen()
    addTen()
    print('score =', score)  # 90
