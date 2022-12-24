# Enter your code here. Read input from STDIN. Print output to STDOUT
A_size, B_size = tuple( map(int, input().split() ) )

group_a = {}

for i in range(A_size):
    char = input()
    if char not in group_a:    group_a[char] = []
    group_a[char].append( str(i+1) )

group_b = []
for j in range(B_size):
    group_b.append( input() )
    
for word in group_b:
    if word in group_a:
        print(' '.join(group_a[word]))
    else:
        print(-1)
    
