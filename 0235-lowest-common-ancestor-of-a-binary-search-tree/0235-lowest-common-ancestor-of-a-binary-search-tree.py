# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ancestors(self, root, node, a=[]):
        if not root:
            return a

        if root.val < node.val:
            return self.ancestors(root.right, node, a+[root])
        elif root.val > node.val:
            return self.ancestors(root.left, node, a+[root])
        else:
            return a+[root]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ancestors = self.ancestors(root, p)+[p]
        q_ancestors = self.ancestors(root, q)+[q]

        n, m = len(p_ancestors)-1, len(q_ancestors)-1

        for i in range(min(n, m), -1, -1):
            if p_ancestors[i] == q_ancestors[i]:
                return p_ancestors[i]
        return root
        

