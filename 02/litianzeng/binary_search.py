#encodinf:utf-8

list_nums=[6, 3, 2, 6, 9, 11, 15, 17, 20, 26, 9, 38, 45, 69, 50, 55, 61, 68, 73]
list_nums.sort()

find_nums=input('数据为{list}\n输入你想查找的数字：'.format(list=list_nums))
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
    print('请输入在',list_nums,'中存在的数字')
