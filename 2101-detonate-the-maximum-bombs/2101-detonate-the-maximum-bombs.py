class Solution:
    def maximumDetonation(self, bombs):
        n, ans, graph = len(bombs), 0, defaultdict(lambda: [])
        
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if bombs[i][2]**2 >= (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2:
                    graph[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))
                          
        return ans