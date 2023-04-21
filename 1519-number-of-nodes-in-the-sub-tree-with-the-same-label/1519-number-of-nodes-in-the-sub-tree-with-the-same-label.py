class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        # storing the total seen characters until the given moment
        count = [0] * 26
        # first_seen is used to store the number of labels equal to the current node's
        # at the moment of the first visit
        first_seen = [-1] * n

        # iterative DFS
        stack = [0]
        while stack:
            node = stack[-1]

            label = ord(labels[node]) - ord('a')
            
            # each node is visited exactly twice
            if first_seen[node] == -1:
                first_seen[node] = count[label]
                count[label] += 1
                
                for neigh in adj_list[node]:
                    if first_seen[neigh] == -1:
                        stack.append(neigh)
            else:
                stack.pop()
                first_seen[node] = count[label] - first_seen[node]
        
        return first_seen