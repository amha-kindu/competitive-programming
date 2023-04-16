# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float('inf')
        def findMaxSum(node):
            if not node:
                return 0
            left = max(findMaxSum(node.left), 0)
            right = max(findMaxSum(node.right), 0)
            self.max_sum = max(self.max_sum, left+right+node.val)
            
            return max(left, right) + node.val
        
        findMaxSum(root)
        return self.max_sum