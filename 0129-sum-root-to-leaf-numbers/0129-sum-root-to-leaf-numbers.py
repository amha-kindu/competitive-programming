# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum_ = 0
        def rootToLeaf(node, path=''):
            if not node:
                return
            if not node.left and not node.right:
                self.sum_ += int(path+str(node.val))
                return
            rootToLeaf(node.left, path+str(node.val))
            rootToLeaf(node.right, path+str(node.val))
        rootToLeaf(root)
        return self.sum_