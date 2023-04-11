from collections import defaultdict

n = int(input())
                                   #SRC  #SNK
count = 0
for i in range(1, n+1):
    temp = input().split()
    for j in range(i, len(temp)):
        if temp[j] == '1':
            count += 1

print(count)


