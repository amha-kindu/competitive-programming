class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        m = len(edges)
        graph = defaultdict(set)
        for i in range(m):
            start, end = edges[i]
            graph[start].add((end, succProb[i]))
            graph[end].add((start, succProb[i]))

        probability = [float("inf")] * n
        heap = [(-1, start_node)]
        visited = set()
        while heap:
            prob, node = heappop(heap)
            visited.add((prob, node))
            for nbr, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob < probability[nbr] and (nbr, new_prob) not in visited:
                    probability[nbr] = new_prob
                    heappush(heap, (new_prob, nbr))

        if probability[end_node] == float('inf') or not probability[end_node]:
            return 0
        return -probability[end_node]
        
        