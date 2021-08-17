# 登入系統
from lab.login.Service import LoginService, LoginError

if __name__ == '__main__':
    service = LoginService()
    username = input('請輸入 username: ')
    password = input('請輸入 password: ')

    try:
        result = service.login(username, password)
        if result == True:
            print('登入成功')
            # 進行登入成功後要做的事 ...
    except LoginError as e:
        print(e)



