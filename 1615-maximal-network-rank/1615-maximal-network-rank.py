class Solution:

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(lambda: set())
        for src, dst in roads:
            graph[src].add(dst)
            graph[dst].add(src)

        max_rank = 0
        for node in graph:
            for other in graph:
                if other == node:
                    continue
                
                rank = len(graph[node]) + len(graph[other])
                if node in graph[other]:
                    rank -= 1
                
                max_rank = max(max_rank, rank)

        return max_rank
        