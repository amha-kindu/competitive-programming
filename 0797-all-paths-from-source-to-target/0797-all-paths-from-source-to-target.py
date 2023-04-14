class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        def dfs(node, path=[0]):
            if node == len(graph)-1:
                self.paths.append(path)
                return

            for neighbor in graph[node]:
                dfs(neighbor, path+[neighbor])
        
        dfs(0)
        return self.paths
