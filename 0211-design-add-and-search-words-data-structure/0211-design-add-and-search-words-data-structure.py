class TrieNode:
  def __init__(self):
    self.childrens = {}
    self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = len(word)
        curr_node = self.root
        for i in range(n):
            if word[i] not in curr_node.childrens:
                curr_node.childrens[word[i]] = TrieNode()
            curr_node = curr_node.childrens[word[i]]
        curr_node.is_end = True
    
    def _search(self, node: TrieNode, word: str, i = 0) -> bool:
        if i == len(word):
            return node.is_end

        if word[i] == '.':
            for child in node.childrens:
                if self._search(node.childrens[child], word, i+1):
                    return True
        elif word[i] in node.childrens:
            return self._search(node.childrens[word[i]], word, i+1)
        return False

    def search(self, word: str) -> bool:
        return self._search(self.root, word)

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)