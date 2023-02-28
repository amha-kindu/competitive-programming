class Solution:
    def scoreDifference(self, nums, left, right, turn=1):
        if left >= right:
            return turn*nums[left]
        
        diff1 = nums[left]+turn*self.scoreDifference(nums, left+1, right, -turn)
        diff2 = nums[right]+turn*self.scoreDifference(nums, left, right-1, -turn)
        
        return turn*max(diff1, diff2)
        
    def PredictTheWinner(self, nums: List[int], turn=0) -> bool:
        return self.scoreDifference(nums, 0, len(nums)-1) >= 0
        
        