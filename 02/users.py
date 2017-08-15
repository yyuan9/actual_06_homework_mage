# encoding:utf-8

users=[]
users_info1='|{0:>20}|{1:>10}|{3:>20}|'
users_info2=users_info1.format('name','age','tel')
while True:
    action=input('please input action(add/find/list/update/exit/detele):')
    if action=='add':
        name=input('请输入用户名：')
        age=input('请输入年龄：')
        tel=input('请输入电话号码：')
        is_exists=False
        for user in users:
            if name==user[0]:
                print('用户添加失败，用户已存在')
                is_exists=True
                break
        if not is_exists:
            users.append((name,age,tel))
            print('添加用户成功')
        print(users)


    elif action=='delete':
        name=input('请输入你要删除的用户名：')
        is_exists=False
        for user in users:
            if name==user[0]:
                users.remove(user)
                print('用户删除成功')
                is_exists=True
                break
        if not is_exists:
            print('删除用户失败，用户不存在')
        print(users)


    elif action=='update':
        name=input('请输入用户名：')
        age=input('请输入年龄：')
        tel=input('请输入电话号码：')
        for i in range(len(users)):
            if name==users[i][0]:
                users[i]=(name,age,tel)
                print('更新用户成功')
                break
            else:
                print('用户更新失败，用户不存在')
        print(users)

#查找用户
    elif action=='find':
        name=input('请输入用户名：')
        is_exists=False
        print(users_info1)
        for user in users:
            if name==user[0]:
                print(users_info2.format(user[0],user[1],user[2]))
                is_exists=True
        if not is_exists:
            print('你输入的用户不存在')
#罗列所有用户
    elif action=='list':
        print(users_info1)
        for user in users:
                print(users_info2.format(user[0],user[1],user[2]))


    elif action =='exit':
        break
    else:
        print('输入错误，请重新输入')
