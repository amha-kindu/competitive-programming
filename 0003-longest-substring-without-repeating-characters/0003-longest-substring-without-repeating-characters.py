
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        answer=0

        subString=set()
        start, end=0, 0
        while end<n:
            if s[end] not in subString:
                subString.add(s[end])
                end+=1
                answer = max(end-start, answer)
            else:
                subString.remove(s[start])
                start+=1
        return answer
        