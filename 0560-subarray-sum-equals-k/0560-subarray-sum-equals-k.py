class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        prefixSumCount = defaultdict(int, {0: 1})
        for i in range(len(nums)):
            running_sum += nums[i]
            if (running_sum - k) in prefixSumCount:
                count += prefixSumCount[running_sum-k]
            prefixSumCount[running_sum]+=1
        return count