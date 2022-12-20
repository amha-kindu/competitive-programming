m, n = list( map(lambda a: int(a), input().split(' ')) )
nums = list( map(lambda a: int(a), input().split(' ')) )
A = set( map(lambda a: int(a), input().split(' ')) )
B = set( map(lambda a: int(a), input().split(' ')) )

happiness = 0
for num in nums:
    if num in A:    happiness += 1
    elif num in B:  happiness -= 1
print(happiness
