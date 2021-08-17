# 基本 輸入input 輸出 print
import math

def myPrint(data):
    print("{:,}".format(float("%.2f" % data)))

if __name__ == '__main__':
    r = input('請輸入半徑: ')
    r = float(r)
    area = r**2 * math.pi

    print("{:,}".format(float("%.2f" % area)))
    myPrint(area)





