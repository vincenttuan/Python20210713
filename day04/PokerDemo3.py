import random as r

def point(p):
    # A -> 1點, J, Q, K -> 0.5點
    if p == 'A':
        return 1
    if p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return int(p)

if __name__ == '__main__':
    pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    # random 內建洗牌
    r.shuffle(pokers)
    print(len(pokers), pokers)
    # 10點半
    a = pokers.pop(0)
    print(a, len(pokers), pokers)
    b = pokers.pop(0)
    print(b, len(pokers), pokers)
    print(a + b)
    print(point(a) + point(b))
