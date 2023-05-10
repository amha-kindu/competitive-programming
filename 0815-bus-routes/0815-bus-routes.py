class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        for bus in range(len(routes)):
            for stop in routes[bus]:
                graph[stop].add(bus)

        visited = set()
        frontier = [source]
        depth = 0
        while frontier:
            for _ in range(len(frontier)):
                stop = frontier.pop(0)
                if stop == target:
                    return depth

                for next_bus in graph[stop]:
                    if next_bus not in visited:
                        frontier.extend(routes[next_bus])
                        visited.add(next_bus)
            depth += 1
        return -1

        