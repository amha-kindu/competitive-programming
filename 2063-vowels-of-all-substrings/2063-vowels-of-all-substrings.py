class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        n = len(word)
        for i, char in enumerate(word):
            if word[i] in ['a', 'e', 'i', 'o', 'u']:
                count += (n - i) * (i + 1)
        return count