# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ancestors, q_ancestors = [], []
        def traverse(node, ancestors =[]):
            nonlocal p_ancestors, q_ancestors
            if not node:
                return
            
            if node == p:
                p_ancestors = ancestors + [node]
            elif node == q:
                q_ancestors = ancestors + [node]

            traverse(node.left, ancestors+[node])
            traverse(node.right, ancestors+[node])
        traverse(root)

        n, m = len(p_ancestors), len(q_ancestors)
        i = 0
        while i < min(n, m) and p_ancestors[i].val == q_ancestors[i].val:
            i += 1
        return p_ancestors[i-1]

