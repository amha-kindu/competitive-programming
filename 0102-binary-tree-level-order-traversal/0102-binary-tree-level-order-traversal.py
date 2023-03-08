# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelTraverse(self, root, level=0):
        if not root:
            return
        self.level_order[level].append(root.val)

        self.levelTraverse(root.left, level+1)
        self.levelTraverse(root.right, level+1)

    def levelOrder(self, root: Optional[TreeNode], level=0) -> List[List[int]]:
        MAX_DEPTH = 2000
        self.level_order = [[] for _ in range(MAX_DEPTH)]

        self.levelTraverse(root)

        empty = self.level_order.index([])
        return self.level_order[:empty]
        
        