#encoding: utf-8
#二分查找
#nums = [1,5,6,13,19,21,30,37,56,64,75,80,88,99]  
print(nums)
number = input("请输入你想查找的元素")
number = int(number)
low = 0
high = len(nums) - 1 

while True:
    if (high+low) % 2 == 0:
        mid = (high+low) / 2
    else:
        mid = (high+low+1) / 2 
    if number > nums[int(mid)]:
        low = mid + 1
    elif number < nums[int(mid)]:
        high = mid - 1
    elif number == nums[int(mid)]:
        print('The number is in the %d position in nums1' % mid)
        break
    if high < low:
        print('Can not find this number in nums1')
        break   
