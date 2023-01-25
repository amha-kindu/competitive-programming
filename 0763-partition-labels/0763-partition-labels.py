class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightMost = {}
        
        for i in range(1, len(s)+1):
            rightMost[s[i-1]] = i
                
        ans = []       
        j, max_i, count = 1, 1, 0
        while j<=len(s):
            if rightMost[s[j-1]] > max_i:  
                max_i=rightMost[s[j-1]]
            if j==max_i:
                ans.append(count+1)
                count=-1
            count+=1
            j+=1
        
        return ans;