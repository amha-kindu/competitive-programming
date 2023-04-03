class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)

        count = 0
        for left in range(n):
            gcd_ = nums[left]
            right = left
            while right < n and gcd_ >= k:
                gcd_ = gcd(gcd_, nums[right])
                if gcd_ == k:
                    count += 1
                right += 1
        return count
        
