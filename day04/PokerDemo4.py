# 10點半，我與電腦對戰版
import random as r


def point(p):  # 取得點數
    # A -> 1點, J, Q, K -> 0.5點
    if p == 'A':
        return 1
    if p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return int(p)


if __name__ == '__main__':
    pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    r.shuffle(pokers)
    # 電腦先拿牌
    pc_1 = pokers.pop(0)
    pc_2 = pokers.pop(0)
    # 玩家拿牌
    play_1 = pokers.pop(0)
    play_2 = pokers.pop(0)
    # 算分數
    pc_score = point(pc_1) + point(pc_2)
    play_score = point(play_1) + point(play_2)
    # 攤牌
    print('PC:', pc_1, pc_2, pc_score)
    print('Player:', play_1, play_2, play_score)
    # Winner ?
    if pc_score > 10.5 and play_score > 10.5:
        print('PC 與 Player 都爆了')
    elif pc_score > 10.5:
        print('PC 爆了, Player 贏了')
    elif play_score > 10.5:
        print('Player 爆了, PC 贏了')
    elif pc_score >= play_score:
        print('PC 贏了')
    else:
        print('Player 贏了')
