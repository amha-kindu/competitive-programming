class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        i, l, r, n, m = 0, 0, 0, len(word1), len(word2)
        while(l<n or r<m):
            if l<n and (i%2==0 or r>=m):  
                merged+=word1[l]
                l+=1
            elif r<m and (i%2!=0 or l>=n): 
                merged+=word2[r]
                r+=1
            i+=1
        return merged
        
        