# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int( input() )
for _ in range(T):
    n = int( input() )
    side_length = list( map(lambda a: int(a), input().split(' ')) )

    l, r = 0, len(side_length)-1
    pile = []
    while(r>=l):
        block = 0
        if side_length[l]>side_length[r]:
            block = side_length[l]
            l+=1
        else:
            block = side_length[r]
            r-=1
        
        if pile:
            if block <= pile[-1]:   pile.append(block)
            else:   break
        else:
            pile.append(block)
           
    if( len(pile) == len(side_length) ):
        print('Yes')
    else:
        print('No')

