from collections import defaultdict

n = int(input())
k = int(input())

graph = defaultdict(lambda: [])
for _ in range(k):
    operation = input().split()
    if operation[0] == '1':
        graph[operation[1]].append(operation[2])
        graph[operation[2]].append(operation[1])
    elif graph[operation[1]]:
        print(*graph[operation[1]], sep=' ')
