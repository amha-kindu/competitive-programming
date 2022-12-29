n = int( input() )


for _ in range(n):
    t_size_a, t_size_b = tuple( input().split() )

    a_len = len(t_size_a)-1
    b_len = len(t_size_b)-1

    if t_size_a[-1]<t_size_b[-1]:
        print('>')
    elif t_size_a[-1]>t_size_b[-1]:
        print('<')
    else:
        if t_size_a[-1] == 'S': 
            if a_len>b_len: print('<')
            elif a_len<b_len: print('>')
        elif t_size_a[-1] == 'L':
            if a_len>b_len: print('>')
            elif a_len<b_len: print('<')
        
        if a_len == b_len: print('=')
