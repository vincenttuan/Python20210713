# 嵌套函式（閉包）

def calc(x):
    def add(y):
        return x + y
    return add

if __name__ == '__main__':
    ten = calc(10)  # x=10 得到 add 函式
    fif = calc(50)  # x=50 得到 add 函式

    print(ten(20))  # y=20 呼叫 add 函式 其中 x=10
    print(fif(20))  # y=20 呼叫 add 函式 其中 x=50
