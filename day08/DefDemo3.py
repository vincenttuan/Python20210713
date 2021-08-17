# 方法參數的預設值
def calc(x=0, y=0):
    print('x=', x)
    print('y=', y)
    print('--------')

if __name__ == '__main__' :

    calc(10, 20)
    calc(10)
    calc(y=20)  # 要給 y
    calc()

