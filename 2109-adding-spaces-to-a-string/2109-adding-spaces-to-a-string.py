class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modified_str = ''
        ptr = 0
        for i in range(len(s)):
            if ptr<len(spaces) and spaces[ptr]==i:
                ptr+=1
                modified_str += " "+s[i]
            else:
                modified_str += s[i]
        return modified_str