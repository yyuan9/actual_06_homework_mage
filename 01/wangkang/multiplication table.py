#encoding: utf-8

for x in range(1,10):
    for y in range(1,x+1):
        print(y,'x',x,'=',y * x,'\t',end='')
    print(end='\n')