class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        for src_, dst_, cst in flights:
            graph[src_].add((dst_, cst))

        # Dijkstra's Algorithm
        min_price = defaultdict(lambda: float('inf'))
        min_price[src] = 0

        heap = [(0, 0, src)]
        visited = set()
        while heap:
            cost, stops, node = heappop(heap)
            if (stops, node) in visited:
                continue
            visited.add((stops, node))
            for nbr, wgt in graph[node]:
                new_cost = cost + wgt
                if (stops < k or nbr == dst):
                    min_price[nbr] = min(min_price[nbr], new_cost)
                    heappush(heap, (new_cost, stops+1, nbr))
            

        return min_price[dst] if min_price[dst] != float('inf') else -1