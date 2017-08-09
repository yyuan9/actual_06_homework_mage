#encoding:utf-8

import random
random_num = random.randint(0,100)
print("这个随机数是：",random_num)

input_num = input("请输入一个数:")
input_num = int(input_num)

i=0
while i<5:

	i += 1

	if input_num < random_num:
		print("猜小了")
	elif input_num > random_num:
		print("猜大了")
	elif input_num == random_num:
		print("恭喜你猜对了")
		break

	if i==5:
		print("太笨了，下次再来")
		break

	input_num = input("请输入一个数:")
	input_num = int(input_num)