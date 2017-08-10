#encoding:utf-8
import random
count = 0
max_count = 5
random_num = random.randint(0,100)
random_num = int(random_num)
print(random_num)
#print(type(random_num))
while True:

    input_random_num=int(input('请输入一个数字，进行猜拳'))
    #print(type(input_random_num))

    count += 1
    if input_random_num == random_num:
        print('猜对了,猜数是:',random_num)
        break
    elif input_random_num < random_num:
        print('猜小了')
    else:
        print('猜大了')
    if count >= max_count:
        print('你真笨，5次已经猜完咯，猜数为:',random_num)
        break
