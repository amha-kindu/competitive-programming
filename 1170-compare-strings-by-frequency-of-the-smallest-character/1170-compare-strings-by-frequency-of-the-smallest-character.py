class Solution:

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(x):
            x = sorted(x)
            return x.count(x[0])

        for i in range(len(words)):
            words[i] = f(words[i])

        answer = []
        for query in queries:
            count = 0
            for word in words:
                if f(query) < word:
                    count += 1
            answer.append(count)
        return answer