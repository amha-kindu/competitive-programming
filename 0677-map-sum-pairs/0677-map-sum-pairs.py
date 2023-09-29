class MapSum:

    def __init__(self):
        self.dict = {}
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.dict[key] = val
        self.trie.insert(key)

    def sum(self, prefix: str) -> int:
        sum_ = 0
        for word in self.trie.wordsWithPrefix(prefix):
            sum_ += self.dict[word]
        return sum_


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

    def getWords(self, node: TrieNode, prefix: str):
        ans = []
        def retrieveWords(node: TrieNode, word=''):
            if node.is_end:
                nonlocal ans
                ans.append(prefix+word)
            for child in node.childrens:
                retrieveWords(node.childrens[child], word+child)
        retrieveWords(node)
        return ans

    def wordsWithPrefix(self, prefix: str) -> List[str]:
        n = len(prefix)
        curr_node = self.root
        for i in range(n):
            if prefix[i] not in curr_node.childrens:
                return []
            curr_node = curr_node.childrens[prefix[i]]
        return self.getWords(curr_node, prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)