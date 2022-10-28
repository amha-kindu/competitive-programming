class Solution:
    def decodeString(self, s: str) -> str:
        l=len(s)
        stack=[]
        substr=[]
        for i in range(l):
            if s[i]=='[':
                stack.append(i)
            elif s[i]==']':
                j=stack.pop()
                while len(substr)>0 and j<substr[-1][1]:
                    substr.pop()
                n=''
                m=1
                while s[j-m].isdigit():
                    n=s[j-m]+n
                    m+=1
                n=int(n)
                substr.append((j,i,n,j-m+1))
        while(len(substr)>0):
            i,j,n,m=substr.pop()
            processed=n*self.decodeString(s[i+1:j])
            s=s[:m]+processed+s[j+1:]
        return s
                 
        