import math

if __name__ == '__main__':
    print("pi:", 3.14)
    print("pi:", math.pi)
    print("1.計算圓面積")
    r = 35
    area = r**2 * math.pi
    print("半徑: %d 圓面積: %.2f" % (r, area))
    print("半徑: %d 圓面積: %s" % (r, format(area, ",")))
    print("半徑: %d 圓面積: %s" % (r, format(int(area*100)/100, ",")))
    print("2.計算球體積")
    area = 4/3 * (r ** 3 * math.pi)
    print("半徑: %d 球體積: %.2f" % (r, area))
    print("半徑: %d 球體積: %s" % (r, format(int(area * 100) / 100, ",")))
