# DAO = Data Access Object
from lab.login.Model import User

class UserDao:

    __users = [
        User('john', '1234'),
        User('mary', '5678')
    ]

    def find_user(self, username):
        for user in self.__users:
            if user.username == username:
                return user
        return None

    # 查詢
    def find_all_user(self):
        return self.__users

    # 新增
    def add_user(self, user):
        self.__users.append(user)

    # 修改 （Homework）


    # 刪除 （Homework）

