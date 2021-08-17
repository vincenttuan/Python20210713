'''
設計二個溫度轉函式 ctof、ftoc
輸入攝氏溫度回傳華式溫度
輸入華式溫度回傳攝氏溫度

公式：
華氏 = 攝氏*(9/5)+32
攝氏 = (華氏-32)*5/9
'''

def ctof(c):
    f = c * (9 / 5) + 32
    return f

def ftoc(f):
    c = (f - 32) * 5 / 9
    return c

if __name__ == '__main__':
    print(ctof(10))
    print(ftoc(50))
