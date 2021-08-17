class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return 'User %s / %s' % (self.username, self.password)

