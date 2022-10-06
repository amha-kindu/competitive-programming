class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        srtd=sorted(arr)
        if srtd==arr:
            return []
        l=0
        flips=[]
        myReverse=lambda k,nums: nums[k::-1]+nums[k+1:]
            
        while l<n:
            m=arr.index(srtd[l])
            if m==l:
                l+=1
                continue
            arr=myReverse(m,arr)
            flips.append(m+1)
            if l!=0:
                w=m-l
                arr=myReverse(w,arr)
                flips.append(w+1)
                arr=myReverse(m,arr)
                flips.append(m+1)
                if arr==srtd:
                    break
            l+=1
        return flips
        