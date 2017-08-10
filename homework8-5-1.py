#encoding:utf-8

i=1
j=1
for i in range(1,10):
	for j in range(1,i+1):
		if i==j:
			print(i,"*",j,"=",i*j)
		else:
			print(i,"*",j,"=",i*j,end=" ")