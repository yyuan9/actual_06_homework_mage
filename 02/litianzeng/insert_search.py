#encoding: utf-8

nums=[6, 3, 2, 11, 15, 17, 20, 26, 9, 38, 45, 69, 50, 55, 61, 68, 73]

for i in range(len(nums)):
    for j in range(i,0,-1):
        if nums[j-1]>nums[j]:
            nums[j-1],nums[j]=nums[j],nums[j-1]

print(nums)
