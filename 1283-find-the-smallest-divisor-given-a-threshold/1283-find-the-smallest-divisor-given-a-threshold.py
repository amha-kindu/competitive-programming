class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        divisor = float('inf')
        
        while right >= left:
            mid = (right + left) // 2
            sum_ = 0

            for num in nums:
                sum_ += ceil(num/mid)
            
            if sum_ > threshold:
                left = mid + 1
            else:
                divisor = min(divisor, mid)
                right = mid - 1

        return divisor
