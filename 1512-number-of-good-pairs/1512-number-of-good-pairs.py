class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        count={}
        ans=0
        for i in range(n):
            g=count.get(nums[i],[])
            for m in g:
                ans+=1
            count[nums[i]]=g+[i]
        return ans