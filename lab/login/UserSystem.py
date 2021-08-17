from lab.login.Service import UserService

def print_users(users):
    for user in users:
        print(user)
    print()

if __name__ == '__main__':
    service = UserService()
    # 查詢所有 user
    users = service.get_users()
    print_users(users)

    # 新增 user
    username = 'helen'
    password = '0000'
    service.add(username, password)

    # 查詢所有 user
    users = service.get_users()
    print_users(users)

    # 修改密碼
    username = 'helen'
    password = '0000'
    new_password = '9999'
    service.update_password(username, password, new_password)

    # 查詢所有 user
    users = service.get_users()
    print_users(users)

    # 刪除 user
    username = 'helen'
    service.delete_user(username)

    # 查詢所有 user
    users = service.get_users()
    print_users(users)
