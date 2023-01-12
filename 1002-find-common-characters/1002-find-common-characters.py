class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for word in words:
            common &= Counter(word)
        return list(common.elements())