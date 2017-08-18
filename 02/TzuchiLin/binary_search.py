#encoding:utf-8
#二分法将数字排序
nums = [6,11,24,32,12,16,15,13]
nums.sort()  # 确保list为有序的

input_num = input("请输入数字: ")
input_num = int(input_num)

start = 0
end = len(nums)-1

while True:
	middle_num =  start + (end-start)//2  #另一种写法middle_num = int(start + (end-start)//2  )
	if input_num == nums[middle_num]:
		print("找到了！ 索引位置是:",middle_num)
		break
	elif input_num > nums[middle_num]: #从middle后面找
		start = middle_num + 1
	else:
		end = middle_num - 1
	if end < start:
		print("没找到！")
		break

	     
