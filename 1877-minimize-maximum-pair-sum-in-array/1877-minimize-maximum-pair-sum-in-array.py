class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairSum=0
        l,r=0,len(nums)-1
        while r>l:
            pairSum=max(pairSum,nums[l]+nums[r])
            l+=1
            r-=1
        return pairSum
        