#encoding: utf-8
import random 
print("Let's start a guess number game!")
random_num=random.randint(0,100)
i=0
while i < 5:
    user_input_number=input("请输入0~100范围内的一个数字：")
    user_input_number=int(user_input_number)
    if user_input_number > random_num:
        print("猜大了。")
    elif user_input_number < random_num:
        print("猜小了。")
    else:
        print("猜对了！")
        break
    i += 1
if i ==5:
    print("太笨了，下次再来。")

