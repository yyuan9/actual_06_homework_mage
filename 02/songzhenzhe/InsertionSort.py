#encoding=utf-8

nums = [11,6,7,9,4,2,1]
print("初始list清单数据：%s" %(nums))

num = input("添加20以内的数字：")
num = int(num)

nums.append(num)

for x in range(len(nums)):
    for y in range(len(nums)-1):
        # print(y)
        if nums[y] > nums[y+1]:
            tmp = nums[y]
            nums[y] = nums[y+1]
            nums[y+1] = tmp
print(nums)