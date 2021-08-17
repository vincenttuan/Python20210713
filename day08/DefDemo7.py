# 不定數量的參數 *
# 類似 java 語言的 vararg ...


def get_sum(*score):  # *score 表示有很多 score
    print(type(score), score, sum(score))


def get_sum_bypass(*score):  # 取得及格分數的總和
    sum = 0
    for s in score:
        if s >= 60:
            sum = sum + s
    print(sum)


def get_sum_bypass2(*score):  # 取得及格分數的總和
    # 建立一個及格分數的列表
    pass_score = [s for s in score if s >= 60]
    print('pass_score:', pass_score, 'sum:', sum(pass_score))


if __name__ == '__main__':
    get_sum(100, 50, 80, 40)
    get_sum_bypass(100, 50, 80, 40)
    get_sum_bypass2(100, 50, 80, 40)
