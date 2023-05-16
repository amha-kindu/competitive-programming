class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node]=False
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return safe[node]
            safe[node]=True
            return safe[node]

        answer = []
        for i in range(n):
            if dfs(i):
                answer.append(i)
            
        return sorted(answer)