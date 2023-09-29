class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.longestWord()

class TrieNode:
  def __init__(self):
    self.childrens = {}
    self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.root.is_end = True

    def insert(self, word: str) -> None:
        n = len(word)
        curr_node = self.root
        for i in range(n):
            if word[i] not in curr_node.childrens:
                curr_node.childrens[word[i]] = TrieNode()
            curr_node = curr_node.childrens[word[i]]
        curr_node.is_end = True

    def longestWord(self) -> str:
        lgst_word = ''
        def find(node, word='', i = 0, prev=True):
            if not node.is_end or not prev:
                return
            if node.is_end:
                nonlocal lgst_word
                if len(word) > len(lgst_word):
                    lgst_word = word
                elif len(word) == len(lgst_word):
                    lgst_word = min(lgst_word, word)
            for child in node.childrens:
                find(node.childrens[child], word+child, i+1, node.is_end)
        find(self.root) 
        return lgst_word
