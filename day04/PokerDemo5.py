import random as r


def point(p):  # 取得點數
    # A -> 1點, J, Q, K -> 0.5點
    if p == 'A':
        return 1
    if p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return int(p)


def getScore(cards): # 計算總分
    score = 0
    for p in cards:
        score = score + point(p)
    return score


def playGame():
    pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4 * 4
    r.shuffle(pokers)

    # 之後透過詢問可以連續拿牌,連續計算分數 (Homework)
    # 遊戲開始User與PC各先拿到一張牌
    my_cards = []  # 目前 user 手中的牌
    my_cards.append(pokers.pop(0))
    pc_cards = []  # 目前 pc 手中的牌
    pc_cards.append(pokers.pop(0))

    # User
    while True:
        # 計算每一張牌的分數
        my_score = getScore(my_cards)
        print("User:", my_cards, my_score)
        # 分數是否超過 10.5
        if(my_score > 10.5):
            print('User 爆了 !')
            break;
        resp = input('User 還要牌嗎(y/n) ? ')
        if resp == 'y':
            my_cards.append(pokers.pop(0))
        else:
            break
    # PC
    while True:
        # 計算每一張牌的分數
        pc_score = getScore(pc_cards)
        print("PC:", pc_cards, pc_score)
        if (pc_score > 10.5):
            print('PC 爆了 !')
            break;
        if pc_score < 7: # 小於 7 點強制補牌
            pc_cards.append(pokers.pop(0))
        else:
            break;

    # Winner ?
    print("User:", my_score, " PC:", pc_score)
    if my_score <= 10.5 and pc_score <= 10.5:
        if my_score > pc_score:
            print("Winner: User")
            return 1
        elif my_score < pc_score:
            print("Winner: PC")
            return -1
        else:
            print("平手")
            return 0
    elif my_score <= 10.5 and pc_score >= 10.5:
        print("Winner: User")
        return 1
    elif my_score > 10.5 and pc_score <= 10.5:
        print("Winner: PC")
        return -1
    else:
        print("平手(都爆了)")
        return 0


