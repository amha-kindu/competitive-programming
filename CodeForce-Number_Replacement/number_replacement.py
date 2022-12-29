n = int( input() )

for _ in range(n):
    nums_len = int( input() )
    nums = input().split()
    string = input()

    mapping = {}
    answer = 'YES'
    for i in range(nums_len):
        if nums[i] not in mapping:
            mapping[nums[i]] = string[i]
        elif mapping[nums[i]]!=string[i]:
            answer= 'NO'
            break
    print(answer)
