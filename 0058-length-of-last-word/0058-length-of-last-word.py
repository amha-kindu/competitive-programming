class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Removing any trailing white spaces
        s = s.strip()
        
        return len( s.split(' ')[-1] )