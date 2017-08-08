#encoding:utf-8

import random
random_num =random.randint(0,100)

count=1
while count<=5:
    ss=input('请在控制台中输入一个数字：')
    ss=int(ss)

    if ss < random_num :
        print('小了，请重试，你还有',5-count,'次机会')
        count=count+1
    elif ss > random_num :
        print('大了，请重试，你还有',5-count,'次机会')
        count=count+1
    else : 
        print('恭喜你！猜对了')
        break
print("游戏结束，请重新开始！")
