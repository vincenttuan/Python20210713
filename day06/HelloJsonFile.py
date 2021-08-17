import json
# 讀/寫檔
# 參數：r 讀, w 寫, encoding='utf-8' 編碼

file = open('people.json', 'r', encoding='utf-8')
str = file.read()  # 將檔案內的資料存放到 str 變數中
print(type(str), str)

x = json.loads(str)  # 將 json 字串轉為 dict 物件
print(type(x), x)

# 請計算並印出所有人的 bmi 值
people = x
for person in people:
    name = person['name']
    w = person['profile']['w']
    h = person['profile']['h']
    bmi = w / pow(h/100, 2)
    print("%s bmi= %.2f" % (name, bmi))
