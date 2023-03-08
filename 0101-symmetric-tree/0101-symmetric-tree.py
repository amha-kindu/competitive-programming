# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertedEqual(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        left_same = self.invertedEqual(p.left, q.right)
        right_same = self.invertedEqual(p.right, q.left)
        
        return (p.val==q.val) and left_same and right_same

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.invertedEqual(root.left, root.right)