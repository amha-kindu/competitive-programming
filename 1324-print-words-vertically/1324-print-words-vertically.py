class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        verticalWords = []
        
        maxLen = max([len(s[i]) for i in range(len(s))])
        
        for char_i in range(maxLen):
            col_word = ''
            for word_i in range(len(s)):
                if char_i<len(s[word_i]):
                    col_word += s[word_i][char_i]
                else:
                    col_word += ' '

            verticalWords.append(col_word.rstrip())
            
        return verticalWords
            