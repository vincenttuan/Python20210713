# __init__
# __call__ 多了 return 可以用

class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Foo (%d, %d)' % (self.x, self.y)

class Bar:
    def __call__(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y

    def __str__(self):
        return 'Bar (%d, %d)' % (self.x, self.y)


if __name__ == '__main__':
    foo = Foo(10, 20)    # __init__
    print(foo)           # __str__

    bar = Bar()          # __init__
    result = bar(30, 40) # __call__
    print(result)
    print(bar)           # __str__

