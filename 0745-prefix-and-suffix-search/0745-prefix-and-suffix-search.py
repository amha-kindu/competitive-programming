class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.indices = defaultdict(list)
        for i in range(len(words)):
            self.trie.insert(words[i])
            self.indices[words[i]].append(i)

    def f(self, pref: str, suff: str) -> int:
        temp = self.trie.wordsWithPrefix(pref)
        ans = -1
        for val in temp:
            if self.indices[val] and val[-len(suff):] == suff:
                ans = max(ans, self.indices[val][-1])
        return ans

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
        ans = set()
        def retrieveWords(node: TrieNode, word=''):
            if node.is_end:
                nonlocal ans
                ans.add(prefix+word)
            for child in node.childrens:
                retrieveWords(node.childrens[child], word+child)
        retrieveWords(node)
        return ans

    def wordsWithPrefix(self, prefix: str) -> List[str]:
        n = len(prefix)
        curr_node = self.root
        for i in range(n):
            if prefix[i] not in curr_node.childrens:
                return set()
            curr_node = curr_node.childrens[prefix[i]]
        return self.getWords(curr_node, prefix)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)