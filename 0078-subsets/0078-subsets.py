class Solution:
    def getSubsets(self, nums, i=-1, path=[]):
        if i >= len(nums):
            return

        self.num_subsets.append(path)

        for j in range(i, len(nums)):
            self.getSubsets(nums, j+1, path+[nums[j]])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.num_subsets = []
        self.getSubsets(nums)

        return self.num_subsets