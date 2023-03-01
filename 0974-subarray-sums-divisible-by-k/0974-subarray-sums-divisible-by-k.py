class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count, running_sum = 0, 0
        prefixCount = defaultdict(int, {0: 1})
        for i in range(n):
            running_sum += nums[i]
            count += prefixCount[running_sum%k]
            prefixCount[running_sum%k]+=1
        return count