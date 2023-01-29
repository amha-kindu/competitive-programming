

n = int(input())
for _ in range(n):
    nums_len = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    left = 0
    remove_cnt = 0
    for i in range(nums_len-1):
        if abs(nums[i]-nums[i+1])<=1:
            remove_cnt += 1

    if remove_cnt + 1 == nums_len:
        print('YES')
    else:
        print('NO')
