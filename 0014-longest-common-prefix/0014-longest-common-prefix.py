class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):  return
        common = strs[0]
        for stg in strs:
            m = len(stg) if len(stg)<len(common) else len(common)
            i, new = 0, ''
            while(i<m and stg[i]==common[i]):
                new += stg[i]
                i+=1
            common = new
            if not common: break
        return common