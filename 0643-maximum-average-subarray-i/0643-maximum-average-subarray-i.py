class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum, wn_sum = -float('inf'), nums[0]
        wn_left, wn_right = 0, 0
        
        while wn_right <= len(nums):
            if wn_right - wn_left + 1 < k:
                wn_right += 1
                wn_sum += nums[wn_right]
                continue

            max_sum = max(max_sum, wn_sum)
            
            if wn_right+1 < len(nums):
                wn_sum += nums[wn_right+1] - nums[wn_left]
            
            wn_right += 1
            wn_left += 1
        return max_sum / k