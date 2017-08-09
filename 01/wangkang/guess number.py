#encoding: utf-8

import random
random_num = random.randint(0,100)
user_num = 0
chance = 5

while user_num != random_num and chance >= 1:
    user_num = float(input('please input a number:'))
    if user_num > random_num:
        print('猜大了')
    elif user_num < random_num:
        print('猜小了')
    else:
        print('猜对了')
        break
    chance -= 1
    if chance > 0:
        print('你还有',chance,'次机会')
    else:
        continue
print('太笨了，游戏结束！正确的数字是',random_num)
