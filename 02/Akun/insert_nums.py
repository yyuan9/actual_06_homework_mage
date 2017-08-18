#encoding: utf-8
#插入排序

nums = [3,1,8,5,9,14,0]
print("插入前列表 = ", nums)
insert_nums = int(input('请输入一个数字:'))
nums.append(insert_nums)
print("插入后列表 = ", nums)

for j in range(len(nums) - 1):
	for i in range(len(nums) - 1):
		if nums[i] > nums[i + 1]:
			nums[i], nums[i + 1] = nums[i + 1], nums[i]
	print(nums)
