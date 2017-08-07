#encoding: utf-8
for i in range(1,10):
    for j in range(1,10):
        if (j<i):
            print("%d*%d=%2d" %(i,j,i*j),end="  ")
        else:
            print("%d*%d=%2d" %(i,j,i*j))
            break 
