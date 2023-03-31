class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return self.gcd(nums[0], nums[-1])
            