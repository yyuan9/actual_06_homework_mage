# encoding=utf-8

nums = [11, 6, 7, 9, 4, 2, 1]
print("初始list清单数据为：%s" % (nums))

str_num = input("是否有意愿，继续往list清单中添加数字？(Y/N)：")
if str_num == "Y" or str_num == "y":
    num = input("请输入0~20以内的任意数字：")
    num = int(num)
    nums.append(num)
else:
    print("世上没回头要可吃，既然错过了，那就正式进入流程了")

for x in range(len(nums)):
    for y in range(len(nums) - 1):
        # print(y)
        if nums[y] > nums[y + 1]:
            tmp = nums[y]
            nums[y] = nums[y + 1]
            nums[y + 1] = tmp

print("最终的list清单展示为：%s" %(nums))
