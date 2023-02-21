n, m = list( map(int, input().split()) )
array_1 = list( map(int, input().split()) )
array_2 = list( map(int, input().split()) )


ptr_1, ptr_2 = 0, 0
while ptr_2 < m:
    while ptr_1 < n and array_1[ptr_1] < array_2[ptr_2]:
        ptr_1 += 1
    print(ptr_1, end=' ')
    ptr_2 += 1
