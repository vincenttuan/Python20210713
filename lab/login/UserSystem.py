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

