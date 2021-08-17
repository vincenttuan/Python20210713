import math

name = "height"
value = 170
print(name, value)  # 中間預設使用空白隔開
print(name, value, sep="=")  # 中間使用 = 隔開

height = "身高"
h = 170
weight = "體重"
w = 60
# 身高=170&體重=60
print(height, h, sep="=", end="&")  # 使用 & 符號結尾
print(weight, w, sep="=")  # 使用預設換行符號結尾

# 資料對齊
print("-------------------------------")
print("%04d" % 7)
print("%04d" % 77)
print("%04d" % 777)
print("%04d" % 7777)
print("%4d" % 7)
print("%4d" % 77)
print("%4d" % 777)
print("%4d" % 7777)
print("%-4d" % 7)
print("%-4d" % 77)
print("%-4d" % 777)
print("%-4d" % 7777)

# 股票資料列表
symbol1 = "2330.TW"
price1 = 650
amount1 = 4500
total1 = price1 * amount1

symbol2 = "1101.TW"
price2 = 53
amount2 = 120
total2 = price2 * amount2

print("-------------------------------")
print(symbol1, price1, amount1, total1)
print(symbol2, price2, amount2, total2)
print("-------------------------------")
print("%-10s%5d%7d%10d" % (symbol1, price1, amount1, total1))
print("%-10s%5d%7d%10d" % (symbol2, price2, amount2, total2))

# 使用 format
print("身高:{0} 體重{1}".format(170.0, 60.0))

# 計算二點間的距離
x1, y1 = 3, 5
x2, y2 = 500, 880

d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print("{}".format(d))
print("{}".format("%.2f" % d))
# "%.2f" % d -> 資料型態 str
print(type("%.2f" % d))
print("{:,}".format(float("%.2f" % d)))
