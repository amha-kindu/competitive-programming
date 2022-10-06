class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class Digits:
            def __init__(self,d):
                self.d=str(d)
            def __lt__(self,o):
                return self.d+o.d>o.d+self.d
            
        r=list(map(Digits,nums))
        r.sort()
        ans=''
        for i in r:
            ans+=i.d
        ans=ans.lstrip('0')
        return ans if ans else '0'
         