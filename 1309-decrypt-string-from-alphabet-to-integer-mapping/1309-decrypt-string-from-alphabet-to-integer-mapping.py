class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {}
        for i in range(26): mapping[i+1] = chr(i+ord('a'))
        
        decrypted, i = '', 0
        while i<len(s):
            if i+2<len(s) and s[i+2]=='#':
                decrypted += mapping[int(s[i]+s[i+1])]
                i+=3
            else:
                decrypted += mapping[int(s[i])]
                i+=1
        return decrypted
                
                