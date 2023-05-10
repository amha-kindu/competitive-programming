class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: [])
        Indegrees = defaultdict(lambda: 0)
        for src, dst in edges:
            Indegrees[dst]+=1
            graph[src].append(dst)

        answer, visited = set(), set()
        for i in range(n):
            if Indegrees[i] == 0:
                answer.add(i)
                visited = set()
            if i not in visited and len(visited) < n:
                frontier = [i]
                while frontier:
                    for _ in range(len(frontier)):
                        node = frontier.pop()
                        for neighbor in graph[node]:
                            if neighbor not in visited:
                                frontier.append(neighbor)
                                visited.add(neighbor)
            elif i in answer:
                answer.remove(i)
        return answer