pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(pokers)
pokers.reverse()
print(pokers)
pokers.sort()
print(pokers)
# 指定牌
print(pokers[0], pokers[5])
# 洗牌
a = pokers[0]
b = pokers[5]
pokers[0] = b
pokers[5] = a
print(pokers)