class Solution:
    def splitString(self, s: str, i=0, splits = []) -> bool:
        if i >= len(s):
           return len(splits) > 1
        
        answer = False
        for j in range(i, len(s)):
            num = int(s[i:j+1])
            if not splits or splits[-1] - 1 == num:
                temp =  self.splitString(s, j+1,  splits+[num])
                answer = answer or temp

            if answer:  break
        
        return answer