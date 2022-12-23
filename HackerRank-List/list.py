if __name__ == '__main__':
    n = int(input())
    nums = []
    
    for _ in range(n):
        command = input().split(' ')
        if command[0]=='insert':
            index = int(command[1])
            nums.insert(index, int(command[2]))
        elif command[0]=='remove':
            nums.remove( int(command[1]) )
        elif command[0]=='print':
            print( nums )
        elif command[0]=='append':
            nums.append(int(command[1]))
        elif command[0]=='sort':
            nums.sort()
        elif command[0]=='pop':
            nums.pop()
        elif command[0]=='reverse':
            nums = list( reversed(nums) )
        
