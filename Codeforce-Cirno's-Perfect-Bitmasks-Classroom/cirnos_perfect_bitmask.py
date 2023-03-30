


for _ in range(int(input())):
    x = int(input())
    if x == 1:
        print(3)
    elif x % 2 != 0:
        print(1)
    else:
        num = x - (x & (x-1))
        if num:
            print(num)
        else:
            print(num+1)
