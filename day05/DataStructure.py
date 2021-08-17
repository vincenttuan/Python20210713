# Python 基本資料結構
# list   列表    (元素內容可以重複, 元素內容可以修改)
# tuple  列表    (唯讀, Fast)
# set    列表    (元素內容不可重複, 元素內容可以修改)
# dict   字典列表 (元素內容可以重複, 元素內容可以修改)

# list 列表
scores = [100, 90, 90, 80]
print('scores:', scores)
scores[1] = 95
scores.append(70)
print('scores:', scores)

# tuple 列表
scores = (100, 90, 90, 80)
print('scores:', scores)
#scores[1] = 95 不可修改元素內容
#scores.append(70) 不可增加元素
print('scores:', scores)

# list 與 tuple 互轉
print(type(scores), scores)
scores = list(scores) # 將 tuple 轉 list
print(type(scores), scores)
scores = tuple(scores) # 將 list 轉 tuple
print(type(scores), scores)

# set 列表
no = [1, 3, 5, 2, 3, 1]
no = set(no)
no.add(7)
no.add(1)
print(type(no), len(no), no)
