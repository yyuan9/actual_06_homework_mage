#encoding: utf-8
print("欢迎进入用户管理系统")
users = []
while True:
    user_exist = ''
    find_user = ''
    delete_user = ''
    update_user = ''
    user_option = input("请输入find[查找用户] || list[列出所有用户] || add[添加用户] || delete[删除用户] || update[更新用户信息] || exit[退出系统]:")
    if user_option == 'add':
        user_name = input("Please enter username:")
        user_age = input("Please enter userage:")
        user_phone = input("Please enter userphone:")
        for user in users:
            if user_name == user[0]:
                print("Error,你添加的用户已存在!")
                user_exist = 'Yes'
                break
        if user_exist != 'Yes':
            users.append((user_name,user_age,user_phone))     
        print()   

    elif user_option == 'delete':
        delete_user_name = input('请输入要删除用户的用户名:')
        for user in users:
            if delete_user_name == user[0]:
                users.remove(user)
                delete_user = 'Yes'
                break
        if delete_user != 'Yes':
            print('Error,您删除的用户不存在')
        print()


    elif user_option == 'update':
        print('请确保要更新信息的用户存在，并直接在下方输入要更新的信息')
        user_name_update = input("Please enter username:")
        user_age_update = input("Please enter userage:")
        user_phone_update = input("Please enter userphone:")
        for user in users:
            if user_name_update == user[0]:
                users.remove(user)
                users.append((user_name_update,user_age_update,user_phone_update))
                update_user = 'Yes'
                break
        if update_user != 'Yes':
            print('Error,用户不存在，无法更新信息！')
        print()

    elif user_option == 'find':
        find_user_name = input('请输入要查找用户的用户名:')
        for user in users:
            if find_user_name == user[0]:
                print("%s:%s,%s:%s,%s:%s" % ('用户名',user[0],'年龄',user[1],'联系方式',user[2]))
                find_user = 'Yes'
                break
        if find_user != 'Yes':
            print('Error,您查找的用户不存在')
        print()

    elif user_option == 'list':
        for user in users:
            print("%s:%s,%s:%s,%s:%s" % ('用户名',user[0],'年龄',user[1],'联系方式',user[2]))
        print()
    elif user_option == 'exit':
        print("退出系统")
        break
    else:
        print("Error,输入错误，请重新输入")
        print()
