# encoding = utf-8

nums = []

for num in range(1, 20, 2):
    nums.append(num)
print("初始nums列表数据为：%s" % (nums))

low = 0
high = len(nums) - 1

val = input("请输入要查找的Value的值：")
val = int(val)

while True:
    mid = (low + high) // 2
    # print(mid)

    if val not in nums:
        print("要查找的Value值，在list中不存在")
        break
    elif nums[mid] == val:
        print("恭喜，Value值对应的索引位置是：%d" % (mid))
        break
    elif nums[mid] < val:
        low = mid + 1
    else:
        high = mid - 1
