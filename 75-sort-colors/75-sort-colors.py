class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        while i<n:
            maxI=0
            maxVal=nums[0]
            for j in range(n-i):
                if nums[j]>maxVal:
                    maxVal=nums[j]
                    maxI=j
            nums[maxI],nums[-i-1]=nums[-i-1],nums[maxI]
             
            i+=1
        