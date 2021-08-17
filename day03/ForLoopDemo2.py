for x in range(1, 11):  # 1~10 (共10個)
    if x % 3 == 0:
        continue
    if x % 8 == 0:
        break
    print(x)
