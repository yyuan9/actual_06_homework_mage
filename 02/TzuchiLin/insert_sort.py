#encoding:utf-8

nums = [6,4,3,5,7,2,10,9]

for j in range(len(nums)-1):
	for i in range(len(nums)-1):
		if nums[i]>nums[i+1]:
			nums[i],nums[i+1] = nums[i+1],nums[i]	

print(nums)