# 跳脫字元
# 我要印出 ' 或 "
print("印出 \"")
print('印出 "')
print('印出 \'')
print("印出 '")

# 換行, tab
print("小明國文分數100分數學分數90分")
print("小明\n國文分數100分\n數學分數90分")
print("小明\n\t國文分數100分\n\t數學分數90分")

# \ 續行符號
a = 10; b = 20; c = 30
d = a * b / c * b - a * a / b + a + b + c + b * a / c
print(d)
d = a * b / c * b \
    - a * a / b + \
    a + b + c + b \
    * a / c
print(d)
