# Python 基本資料結構
# list   列表    (元素內容可以重複, 元素內容可以修改)
# tuple  列表    (唯讀, Fast)
# set    列表    (元素內容不可重複, 元素內容可以修改)
# dict   字典列表 (元素內容可以重複, 元素內容可以修改)

# dict 字典列表 (key:value)
# key 的值不可以重複
# value 的值可以重複
scores = {'國文':100, '數學':90, '英文':90, '數學':60}
print('全科:', scores)
print('數學:', scores.get('數學'))
print('科目(keys):', scores.keys())
print('分數(values):', scores.values())

# update (合併二個 dict)
scores1 = {'國文':100, '數學':90}
scores2 = {'英文':70, '歷史':58, '國文':90}
scores1.update(scores2)
print(scores1)

# 總分與平均?
scores = scores1.values()
print(type(scores), scores)
print(list(scores))
scores = list(scores)
scoresSum = sum(scores)
print(scoresSum, scoresSum/len(scores))

# for-in
sumScore = 0
scores = {'國文':100, '數學':90, '英文':90, '數學':60}
print(scores)
for key in scores:
    print(type(key), key, scores[key])
    sumScore = sumScore + scores[key]
print(sumScore, sumScore/len(scores))
