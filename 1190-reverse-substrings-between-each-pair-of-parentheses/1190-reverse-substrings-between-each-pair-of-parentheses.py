class Solution:
    def reverseParentheses(self, s: str) -> str:
        parentheses=[]
        for c in range(len(s)):
            if s[c]=='(':
                parentheses.append(c)
            elif s[c]==')':
                s=s[:parentheses[-1]]+s[c:parentheses[-1]:-1]+s[c:]
                parentheses.pop()
        s=s.replace('(','')
        return s.replace(')','')
