# -*- coding:utf-8 -*-
import random
print("猜数字游戏开始了！")
#random.randint(a, b),n: a <= n <= b
random_num = random.randint(0,100)

i=0
while i<5:
	input_num = input("請猜一个数字，范围为1~100：")
	input_num = int(input_num)
	if input_num < random_num:
		print("猜小了")
	elif input_num > random_num:
		print("猜大了")
	else:
		print("恭喜！猜对了！") 
		break
	i+=1		
if i==5:
	print("太笨了，下次再来！正确值是:",random_num)



