from collections import defaultdict

n = int(input())
                                   #SRC  #SNK
source_sink = defaultdict(lambda: [True, True])
for i in range(1, n+1):
    temp = input().split()
    for j in range(1, len(temp)+1):
        if temp[j-1] == '1':
            source_sink[i][1] = False
            source_sink[j][0] = False

sources = []
sinks = []
for node in range(1, n+1):
    is_src, is_snk = source_sink[node]
    if is_src and is_snk:
        sources.append(node)
        sinks.append(node)
    elif is_src:
        sources.append(node)
    elif is_snk:
        sinks.append(node)

print(len(sources), *sorted(sources), sep=' ')
print(len(sinks), *sorted(sinks), sep=' ')

