# -*- encoding = utf-8 -*-

''' 打印九九乘法口诀 '''

for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%2d"%(x,y,x*y),end=" ")
    print()