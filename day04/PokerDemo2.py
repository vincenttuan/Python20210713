import random as r
pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print("洗牌前:", pokers)
print(len(pokers))
# 連續洗牌 n 次
for x in range(len(pokers)):
    n1 = r.randint(0, len(pokers) - 1)
    n2 = r.randint(0, len(pokers) - 1)
    #print(n1, n2, pokers[n1], pokers[n2])
    a = pokers[n1]
    b = pokers[n2]
    pokers[n1] = b
    pokers[n2] = a
print("洗牌後:", pokers)
