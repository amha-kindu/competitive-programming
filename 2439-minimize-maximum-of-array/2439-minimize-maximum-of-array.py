class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        answer = nums[0]
        sum_ = nums[0]
        for i in range(1, n+1):
            answer = max(answer, ceil(sum_ / i))
            sum_ += nums[i] if i < n else 0
        return answer