#encoding: utf-8

raw_nums = [7 ,5 ,101 ,91 ,4 ,8 , 1]

print('原始清单: ', raw_nums)

n = input('请输入一个数字：')
n = int(n)

raw_nums.append(n)

for zz in range(len(raw_nums) - 1):
    
    for xx in range(len(raw_nums) - 1):
        if raw_nums[xx] > raw_nums[xx + 1]:
            tmp = raw_nums[xx]
            raw_nums[xx] = raw_nums[xx + 1]
            raw_nums[xx + 1] = tmp

print('----新清单----\n', raw_nums)
