class Solution:
    def getMaxBitwiseOR(self, nums, i=0, bitwise_or=0, path=[]):
        n = len(nums)
        if i >= n:
            self.bitwiseORs.append(bitwise_or)
            return bitwise_or

        # Take it
        choice1 = self.getMaxBitwiseOR(nums, i+1, bitwise_or | nums[i], path+[nums[i]])

        # Leave it
        choice2 = self.getMaxBitwiseOR(nums, i+1, bitwise_or, path)
        
        return max(choice1, choice2)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.bitwiseORs = []

        max_val = self.getMaxBitwiseOR(nums)

        return self.bitwiseORs.count(max_val)
