list_nums=[2,8,52,36,58,68,47,42,89,92]
list_nums.sort()

find_nums=input('排序后的列表为\n{list}\n输入查找的数字：'.format(list=list_nums))
find_nums=int(find_nums)

low=0
high=len(list_nums)

if find_nums in list_nums:
    while True:
        mid=(low+high)//2
        if find_nums>list_nums[mid]:
            low=mid+1

        elif find_nums<list_nums[mid]:
            high=mid-1

        else:
            find_nums=list_nums[mid]
            print('查找的数字{0}索引位置为{1}'.format(find_nums,mid))
            break

else:
    print('请输入',list_nums,'中存在的数字')