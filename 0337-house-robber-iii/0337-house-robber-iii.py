# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    @lru_cache(None)
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Do not rob this house
        option1 =  self.rob(root.left)+self.rob(root.right)
        
        # Rob this house
        option2 = 0
        if root.left:
            option2 = self.rob(root.left.left)+self.rob(root.left.right)
        if root.right:
            option2 += self.rob(root.right.left)+self.rob(root.right.right)

        return max(option1, option2+root.val)
        