'''
*
**
***
****
*****
'''
# 利用 for-in 將上圖印出

for x in range(1, 6):
    for y in range(0, x):
        print("*", end="")
    print()
