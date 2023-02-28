class Solution:
    def playerOneScore(self, nums, left, right, turn=1):
        if left > right:
            return 0

        choice1 = self.playerOneScore(nums, left+1, right, -turn)
        choice2 = self.playerOneScore(nums, left, right-1, -turn)
        
        if turn==1:
            return max(choice1+nums[left], choice2+nums[right])
        else:
            return min(choice1, choice2)
        
    def PredictTheWinner(self, nums: List[int], turn=0) -> bool:
        n = len(nums)
        totalScore = sum(nums)
        p1_score = self.playerOneScore(nums, 0, n-1)
        p2_score = totalScore - p1_score
        
        return p1_score - p2_score >= 0
        
        