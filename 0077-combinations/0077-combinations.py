class Solution:
    def setCombinations(self, k, nums, i=0, path=[]):
        if len(path) == k:
            self.combinations.append(path)
            return

        if i >= len(nums):
            return

        # Take the current value
        self.setCombinations(k, nums, i+1, path+[nums[i]])     

        # Leave the current valaue
        self.setCombinations(k, nums, i+1, path)     

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        self.setCombinations(k, [i for i in range(1, n+1)])
        return self.combinations
        


        