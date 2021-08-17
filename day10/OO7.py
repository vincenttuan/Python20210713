'''
關於物件的比較的覆寫方法
__lt__ 是 < 小於
__le__ 是 <= 小於等於
__gt__ 是 > 大於
__ge__ 是 >= 大於等於
__eq__ 是 == 等於
'''

class Drink:
    __prices = {'milk': 80, 'coffee':110}
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.price = self.__prices.get(name)
        self.total = self.price * amount

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __str__(self):
        return '%s 數量: %d 單價: $%d 小計: $%d' % \
               (self.name, self.amount, self.price, self.total)

if __name__ == '__main__':
    milk = Drink('milk', 3)
    print(milk)
    coffee = Drink('coffee', 2)
    print(coffee)
    print(milk < coffee)
    print(milk > coffee)
    if milk < coffee:
        print('milk 單價比 coffee 便宜')
    else:
        print('milk 單價比 coffee 貴')
