class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sim_count = {}
        for word in words:
            temp = tuple( sorted( list( set(word) ) ) )
            sim_count[temp] = sim_count.get(temp, 0) + 1

        result = 0
        for i in sim_count.values():
            result += i*(i-1)/2
        return int(result)
            