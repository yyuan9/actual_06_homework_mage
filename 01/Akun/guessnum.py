#encoding: utf-8

import random
random_num = random.randint(0, 100)

num = input("please input a num:")
num = int (num)

i = 0
while num != random_num and i < 6:
	if num < random_num:
		print("猜小了")
	elif num > random_num:
		print("猜大了")
	i = i + 1
	if num == random_num:
		print("猜对了，结束程序")
	else:
		print("太笨了，下次再来")
