#encoding:utf-8
for i in range(0,10):
    for j in range(10 , 0 , -1):
        if i > j:
            print(i,' * ',j,' = ',i * j,end='\t')
    print()
