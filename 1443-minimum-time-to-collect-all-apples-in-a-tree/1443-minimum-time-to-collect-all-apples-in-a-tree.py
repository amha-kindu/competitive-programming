class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph= defaultdict(lambda: [])
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        self.visited_edges = set()
        def dfs(node, visited=set(), path=[]):
            if hasApple[node]:
                self.visited_edges.update(path)
                path = []

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    temp = dfs(neighbor, visited, path+[(node, neighbor)])
                    if temp:
                        return  temp
            return []

        dfs(0)
        return len(self.visited_edges) * 2
                
        