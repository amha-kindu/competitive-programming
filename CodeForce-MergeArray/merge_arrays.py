
n, m = list(map(int, input().split()))
array_1 = list(map(int,input().split(' ')))
array_2 = list(map(int, input().split(' ')))

ptr_1, ptr_2 = 0, 0
while ptr_1<n or ptr_2<m:
    value_1 = array_1[ptr_1] if ptr_1<n else float('inf')
    value_2 = array_2[ptr_2] if ptr_2<m else float('inf')
    if value_1 < value_2:
        print(value_1, end=' ')
        ptr_1+=1
    else:
        print(value_2, end=' ')
        ptr_2+=1
    
