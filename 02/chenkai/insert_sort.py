#encoding: utf-8
#插入排序
#有一个已经排序完成的序列，当用户输入一个数字时，按照升序将元素插入。
nums = [2, 4, 5, 10, 12]  
find_index = ''
number = input('Please enter a number:')
number =int(number)

for num in nums:
    if number <= num:
        nums.insert(nums.index(num),number)
        find_index = 'Yes'
        break
if find_index != 'Yes':
    nums.append(number)
print(nums)

'''    
for i in range(len(nums)):
    if number <= nums[i]:
        nums.insert(i,number)
        find_index = 'Yes'
        break
if find_index != 'Yes':
    nums.append(number) 
print(nums)
'''