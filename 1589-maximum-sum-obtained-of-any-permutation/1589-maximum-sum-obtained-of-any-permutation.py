class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int: 
        n = len(nums)
        zeros = [0] * n
        for start, end in requests:
            zeros[start] += 1
            if end+1 < n:
                zeros[end+1] -= 1
        
        for i in range(1, n):
            zeros[i] += zeros[i-1]

        nums.sort()
        zeros.sort()

        max_sum = 0
        for i in range(n):
            max_sum += zeros[i] * nums[i]

        return max_sum % 1000000007



