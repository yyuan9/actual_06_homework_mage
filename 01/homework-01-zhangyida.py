#encoding:utf-8
'''
Question 1
'''
print("kk")


print("kk",end="")


'''
Question 2   ---打印乘法口诀
'''

raw = 1



while raw <= 9:
	col = 1
	while col <= 9:
		if raw >= col:
		   print(raw , "*" , col , "=" , raw*col , end="\t")
		col += 1
	raw += 1
	print(" ")

    
		







'''
Question 3
1.定义随机数
2.定义input
3.input进行数据转换
4.for循环+if语句
5.5次没有猜中，直接打印
'''
import random

random_num = random.randint(0,100)



for i in range(0,5):
	guess_num = input("please enter your num:")
	guess_num = int(guess_num)

	if guess_num < random_num:
		print("small")
		continue
	elif guess_num > random_num:
		print("big")
		continue
	elif guess_num == random_num:
		print("right , you win")
		break
	

print("too stupid , try next time")





	    



    





