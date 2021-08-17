import time

if __name__ == '__main__':
    print('幸福大廈共有1~7層樓')
    current_floor = 1  # 現在樓層
    while True:
        # 想要去的樓層
        target_floor = input('您現在在 %d 樓。請問要去哪一樓(輸入 0 可離開電梯)？' % (current_floor))
        target_floor = int(target_floor)

        # 判斷 target_floor
        if target_floor == 0:
            break # 離開電梯

        if target_floor == current_floor:
            continue  # 重新選擇

        if target_floor < 1 or target_floor > 7:
            print('請輸入介於 1-7 的整數')
            continue

        if target_floor > current_floor:
            print('電梯上樓')
            while target_floor > current_floor:
                print(current_floor)
                current_floor = current_floor + 1 # 現在樓層每次 + 1
                time.sleep(1)
            print(current_floor) # 到達指定樓層
        else:
            print('電梯下樓')
            while target_floor < current_floor:
                print(current_floor)
                current_floor = current_floor - 1 # 現在樓層每次 - 1
                time.sleep(1)
            print(current_floor)  # 到達指定樓層