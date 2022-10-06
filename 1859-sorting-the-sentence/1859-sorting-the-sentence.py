class Solution:
    def sortSentence(self, s: str) -> str:
        g=s.split(' ')
        words=[]
        for i in g:
            words.append((int(i[-1]),i[:-1]))
        words.sort()
        original=''
        for i in words:
            original+=i[1]+' '
        return original.strip()
        
        