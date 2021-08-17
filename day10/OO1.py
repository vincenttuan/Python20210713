class Human:  # 設計類別
    name = ''
    age = 0
    sex = ''

    def __str__(self) -> str:
        return self.name + ', ' + str(self.age) + ', ' + self.sex


if __name__ == '__main__':
    h1 = Human()  # 建立物件
    h1.name = 'John'
    h1.age = 18
    h1.sex = '男'

    h2 = Human()
    h2.name = 'Mary'
    h2.age = 18
    h2.sex = '女'

    print(h1, h2)
    print(h1.name, h1.age, h1.sex)
    print(h2.name, h2.age, h2.sex)