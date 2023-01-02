class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upperCaseCount = 0
        for char in word:
            if char.isupper():
                upperCaseCount += 1
                
        return upperCaseCount==0 or upperCaseCount == len(word) or upperCaseCount == 1 and word[0].isupper()