# 服務登入所有相關作業
from lab.login.Dao import UserDao
from lab.login.Model import User


class LoginError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return '登入錯誤的原因: %s' % self.message

class LoginService:
    __dao = UserDao()
    def login(self, username, password):
        # 先檢查是否有此人 ?
        user = self.__dao.find_user(username)
        if(user is None):
            e = LoginError('查無此人')
            raise e
        else:
            # 檢查密碼
            if user.password == password:
                return True
            else:
                e = LoginError('登入失敗')
                raise e

class UserService:
    __dao = UserDao()
    def add(self, username, password):
        user = User(username, password)
        self.__dao.add_user(user)

    def get_users(self):
        return self.__dao.find_all_user()


