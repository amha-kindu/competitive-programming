class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefixSumCount = defaultdict(int, {0:1})
        running_sum = 0
        count = 0
        for i in range(n):
            running_sum += nums[i]
            if running_sum-goal in prefixSumCount:
                count += prefixSumCount[running_sum-goal]
            prefixSumCount[running_sum]+=1
        return count