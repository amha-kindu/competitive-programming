class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right=0, len(height)-1
        max_vol=0
        
        while (right>left):
            
            new_vol=min(height[right], height[left])*(right-left)
            
            max_vol=max(max_vol, new_vol)
            
            if(height[left]>height[right]):
                right-=1
            else:
                left+=1

        return max_vol