import time
# Nine table 9x9 乘法表
# 雙重回圈
'''
1x1=1 1x2=2  ... 1x9=9
2x1=2 2x2=4  ... 2x9=18
...
9x1=9 9x2=18 ... 9x9=81
'''

# 1x1=1 1x2=2  ... 1x9=9
# x*y=sum

for x in range(1, 10):
    for y in range(1, 10):
        sum = x * y
        print("%d x %d = %d" % (x, y, sum), end="\t")
        #time.sleep(0.1)
    print()



