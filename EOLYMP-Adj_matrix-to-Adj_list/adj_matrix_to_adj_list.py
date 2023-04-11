from collections import defaultdict

n = int(input())

graph = defaultdict(lambda: [])
for i in range(n):
    temp = input().split()
    for j in range(len(temp)):
        if temp[j]=='1':
            graph[i+1].append(int(j)+1)

for node in graph:
    print(len(graph[node]), end=' ')
    print(*graph[node], sep=' ')
