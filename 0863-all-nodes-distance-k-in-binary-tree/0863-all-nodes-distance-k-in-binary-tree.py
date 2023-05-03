# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(lambda: [])
        def InOrder(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                InOrder(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                InOrder(node.right)

        InOrder(root)
        frontier = [target]
        visited = set(frontier)
        depth = 0
        while frontier:
            if depth == k:
                return [node.val for node in frontier]
            for _ in range(len(frontier)):
                node = frontier.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        frontier.append(neighbor)
                        visited.add(neighbor)
            depth += 1

        return []


