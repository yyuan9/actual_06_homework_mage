#encoding: utf-8
import random
random_num = random.randint(0,100)

i=1
while i <= 5:
    a = int(input("请输入数字："))
    if a > random_num:
        print("大了")
    elif a < random_num:
        print("小了")
    else:
        print("猜对了")
        break
    i+=1 
if i == 6:   
    print("太笨了")
