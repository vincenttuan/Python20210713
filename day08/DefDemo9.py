# 寫一個方法能夠自動將列表裡面的及格分數自動 +20%
# 例如：scores = [50, 60, 70]
# 變成：scores = [50, 72, 84]

def addPass(scores):
    for i in range(0, len(scores)):
        if scores[i] >= 60:
            scores[i] *= 1.2

if __name__ == '__main__':
    scores = [50, 60, 70]
    print(scores)
    addPass(scores)
    print(scores)
