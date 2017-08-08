import random

random_num = random.randint(0,100)
print(random_num)
input_num = input("请输入你猜想的数字：")
i = 1
while i <= 5:
    if int(input_num) < random_num:
        print("猜小了")
        i = i+1
        input_num = input("请输入你猜想的数字：")
        print(i)
    elif int(input_num) > random_num:
        print("猜大了")
        i += 1
        input_num = input("请输入你猜想的数字：")
        print(i)
    elif int(input_num) == random_num:
        print("猜对了")
        break
else:
        print("太笨了，下次再来")

