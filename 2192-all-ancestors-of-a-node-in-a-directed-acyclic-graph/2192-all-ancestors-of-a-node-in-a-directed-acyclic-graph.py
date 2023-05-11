class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        Indegree = defaultdict(int)
        for src, dst in edges:
            graph[src].append(dst)
            Indegree[dst] += 1
        
        queue = []
        for i in range(n):
            if Indegree[i] == 0:
                queue.append(i)

        ancestors = [set() for _ in range(n)]
        while queue:
            node = queue.pop(0)   

            for nextNode in graph[node]:
                Indegree[nextNode] -= 1

                ancestors[nextNode].add(node)
                if ancestors[node]:
                    ancestors[nextNode].update(ancestors[node])

                if Indegree[nextNode] == 0:
                    queue.append(nextNode)
                    
        return [sorted(nums) for nums in ancestors]                        