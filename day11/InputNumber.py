def input_number():
    try:
        x = int(input('請輸入數字: '))
        print('您輸入的是:', x, '平方後＝', x ** 2)
    except ValueError as e:
        print('錯誤原因:', e)
        print('請重新輸入')
        input_number()

if __name__ == '__main__':
    input_number()




