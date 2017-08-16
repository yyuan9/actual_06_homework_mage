l=[6,11,7,9,4,2]
def insert_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1,len(l)):
                if l[min_index] > l[j]:
                    min_index = j
        tmp = l[i]
        l[i] = l[min_index]
        l[min_index] = tmp
    print("result: " + str(l))
insert_sort(l)
print("insert_sort success!!!")