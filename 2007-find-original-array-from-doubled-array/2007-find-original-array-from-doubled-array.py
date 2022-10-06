class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans=[]

        queue=[]
        for num in changed:
            if not queue or num/2!=queue[0]:
                queue.append(num)
            else:
                ans.append(queue.pop(0))
                
        return [] if queue else ans
        
        '''
        count={}
        for i in set(changed):
            count[i]=changed.count(i)
        for m in changed:
            f=count[m]
            if f>0:
                ans.append(m)
                count[m]=f-1
                count[2*m]=count.get(2*m,0)-1
        '''
        # return ans if len(ans)==n//2 else []