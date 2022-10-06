class Solution:
    def isValid(self, s: str) -> bool:
        c={'(':')','{':'}','[':']'}
        stack=[]
        for i in s:
            if i in c:
                stack.append(i)
            elif stack and c[stack[-1]]==i:
                stack.pop()
            else:
                return False
        return stack==[]
                
                
        