import keyword

h, w, score, valid, name = 170.0, 65.5, 90, True, "小明"
print(h, type(h))
print(w, type(w))
print(score, type(score))
print(valid, type(valid))
print(name, type(name))

# 保留字
print(keyword.kwlist)

# 刪除變數 ?
amount = 100
print("amount: ", amount)

del amount

print("amount: ", amount) # 錯誤訊息：amount' is not defined