import math as m


# 設計一個方法透過一個參數 r 就可以得到圓面積與球體積
def calcCircleArea(r):
    # 圓面積
    area = m.pow(r, 2) * m.pi
    # 球體積
    volumn = 4/3 * m.pow(r, 3) * m.pi
    return area, volumn

if __name__ == '__main__':
    r = 10.0
    area, volumn = calcCircleArea(r)
    print('圓面積:', area)
    print('球體積:', volumn)

