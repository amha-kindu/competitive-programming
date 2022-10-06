class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m=len(l)
        ans=[False for _ in range(m)]
        for i in range(m):
            h=nums[l[i]:r[i]+1]
            h.sort()
            n=len(h)
            d=h[1]-h[0]
            arti=True
            for m in range(n-1):
                if h[m+1]-h[m]!=d:
                    arti=False
                    break
            ans[i]=arti

        return ans