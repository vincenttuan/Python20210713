class Number:
    n = 0
    def __init__(self, n):
        self.n = n

    def __add__(self, x):
        self.n = self.n + x

    def __pow__(self, power, modulo=None):
        self.n = pow(self.n, power)

    def __str__(self):
        return str(self.n)

if __name__ == '__main__':
    n = Number(4)
    n + 10
    n ** 2
    print(n)