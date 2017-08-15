# encoding=utf-8

users = []

while True:
    str = input("请输入要操作的功能名称(find/list/add/delete/update/exit): ")

    if str == "add":
        print("请完善下述信息项")
        name = input("请输入用户名：")
        age = input("请输入年龄：")
        mobile = input("请输入联系方式：")

        user_tuple = (name, age, mobile)

        is_exists = False

        for user in users:
            if user[0] == user_tuple[0]:
                print("添加用户失败，失败原因：用户名已存在")
                is_exists = True
                break

        if not is_exists:
            users.append(user_tuple)
            print("添加用户成功")

    elif str == "delete":

        is_exists = False

        name = input("请输入要删除的用户名：")
        for user in users:
            if user[0] == name:
                users.remove(user)
                is_exists = True
                print("删除用户信息成功")
                break

        if not is_exists:
            print("用户数据不存在")

    elif str == "update":
        print("请输入下述信息项")
        name = input("请输入用户名：")
        age = input("请输入年龄：")
        mobile = input("请输入联系方式：")

        user_tuple = (name, age, mobile)

        is_exists = False

        for user in users:
            if user[0] == user_tuple[0]:
                users.remove(user)
                users.append(user_tuple)
                is_exists = True
                print("更新用户%s的资料信息成功" % (name))
                break

        if not is_exists:
            print("用户信息不存在")

    elif str == "find":
    	name = input("请输入要查找的用户名：")
    	for user in users:
    		if user[0] == name:
    			print(user)

    elif str == "list":
        for i in users:
            print(i)

    elif str == "exit":
        print("程序将退出，感谢使用")
        break
