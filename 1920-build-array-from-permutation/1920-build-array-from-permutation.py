class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(len(nums)):
            array.append(nums[nums[i]])
        return array