# 使用 @ 裝飾修飾字

def hotDog(func):
    print('我是熱狗')
    return func

def egg(func):
    print('我是雞蛋')
    return func

def ham(func):
    print('我是火腿')
    return func

@hotDog
@egg
@ham
def bread():
    print('我是麵包')

if __name__ == '__main__':
    bread()
