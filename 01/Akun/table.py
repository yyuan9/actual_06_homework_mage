#encodin: utf-8
#乘法表

tables =input('please input your print table')
print('Here is your table:')

j = 1

while j <= 9:
	i = 1
	while i <= 9:
		if j >= i:
			print(j, '*', i, '=', j * i, end=' ')
		i += 1
	j += 1
	print(' ')
