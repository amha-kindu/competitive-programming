class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        scores = []
        for word in words:
            curr = trie.root
            score = 0
            for char in word:
                curr = curr.childrens[char]
                score += curr.prefix_cnt
    
            scores.append(score)
        return scores

        
class TrieNode:
  def __init__(self):
    self.childrens = {}
    self.is_end = False
    self.prefix_cnt = 0

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
            curr_node.prefix_cnt += 1
        curr_node.is_end = True