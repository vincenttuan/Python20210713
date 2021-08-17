import math as m

# 資料的轉換
chinese = "90"
math    = "80"
english = "100"

sum = chinese + math + english  # 「+」 對於字串而言是連接符號
print("sum = ", sum)

print(type(chinese), type(math), type(english))
sum2 = int(chinese) + int(math) + int(english)
print("sum2 = ", sum2)

# 資料的轉換(Lab)
# 求 bmi 取到小數點 2 位
h, w = "180.5", "85"
print(type(h), type(w))
h = float(h)
w = float(w)
print(type(h), type(w))
bmi = w / (h/100)**2
bmi = w / m.pow(h/100, 2)
print(bmi, bmi)
print("%.2f" % bmi )

