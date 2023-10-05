class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm
        graph = defaultdict(set)
        for src, dst, wgt in times:
            graph[src].add((dst, wgt))

        min_time = [float('inf')]*n
        min_time[k-1] = 0
        queue = [(0, k)]
        visited = set()
        while queue:
            curr_dst, node = heappop(queue)
            visited.add(node)
            for nbr, wgt in graph[node]:
                if curr_dst + wgt < min_time[nbr-1] and nbr not in visited:
                    min_time[nbr-1] = curr_dst + wgt
                    heappush(queue, (curr_dst + wgt, nbr))

        ans = max(min_time)
        return ans if ans != float('inf') else -1