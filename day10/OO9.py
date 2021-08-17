class USD:
    def __get__(self, instance, owner):
        ntd = instance.ntd
        return ntd / 30.5

class JPY:
    def __get__(self, instance, owner):
        ntd = instance.ntd
        return ntd / 0.28

class Exchange:
    usd = USD()
    jpy = JPY()
    def __init__(self, ntd) -> None:
        self.ntd = ntd

if __name__ == '__main__':
    ex = Exchange(10000)
    print(ex.usd)
    print(ex.jpy)
