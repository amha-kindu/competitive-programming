class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs=0
        count={}
        for j in nums:
            count[j]=count.get(j,0)+1
        for i in nums:
            o=0 if k-i!=i else 1
            if k-i in count and count[k-i]>o and count[i]>0:
                pairs+=1
                count[i]-=1
                count[k-i]-=1
        return pairs