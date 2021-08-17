def subTotal(price=None, amount=None):
    if price is None or amount is None:
        print('price 與 amount 必須要有資料')
        return
    total = price * amount;
    print('total:', total)

if __name__ == '__main__':

    subTotal(100, 50)
    subTotal(amount=100)
