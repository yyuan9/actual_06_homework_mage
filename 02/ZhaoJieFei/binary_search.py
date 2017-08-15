#encoding: utf-8

print('--------------------\n原始序列：以1为起始值，101为终止值，步长为4的序列\n--------------------')

raw_nums = []

for zz in range(1, 102, 4):
    raw_nums.append(zz)

low = 0
high = len(raw_nums) - 1

n = input("请输入要查找的数值：")
val = int(n)

while True:
    mid = (low + high) // 2

    if val not in raw_nums:
        print("要查找的数值，不在原始序列中！")
        break
    elif raw_nums[mid] == val:
        print("恭喜！该数值对应的索引位置是：%d" %(mid))
        break
    elif raw_nums[mid] < val:
        low = mid + 1
    else:
        high = mid - 1
