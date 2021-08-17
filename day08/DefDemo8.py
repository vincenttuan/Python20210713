# 寫一個方法能夠自動將列表裡面的分數自動+10
# 例如：scores = [50, 60, 70]
# 變成：scores = [60, 70, 80]

def add(scores, x):
    for i in range(0, len(scores)):
        scores[i] += 10

def add(x):
    global scores
    for i in range(0, len(scores)):
        scores[i] += 10

if __name__ == '__main__':
    scores = [50, 60, 70]
    print(scores)
    #add(scores, 10)
    add(10)
    print(scores)
