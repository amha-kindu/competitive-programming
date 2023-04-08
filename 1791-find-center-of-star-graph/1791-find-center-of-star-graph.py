class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(lambda: [])
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        V = len(graph.keys())
        for node in graph:
            if len(graph[node]) == V - 1:
                return node