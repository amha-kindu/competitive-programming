class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        Indegrees = defaultdict(lambda: 0)
        for src, dst in edges:
            Indegrees[dst]+=1

        answer = set()
        for i in range(n):
            if Indegrees[i] == 0:
                answer.add(i)
        return answer