class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        second_largest = None

        mono = []
        left, right = 0, n-1
        while right >= 0:
            while mono and mono[-1] < nums[right]:
                second_largest = mono.pop()
                
            if second_largest and nums[right] < second_largest:
                return True
            mono.append(nums[right])
            right -= 1
        return False
