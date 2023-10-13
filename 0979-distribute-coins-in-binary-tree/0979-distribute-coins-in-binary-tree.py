# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def distribute(root):
            if not root:
                return 0
            coins = root.val - 1 + distribute(root.left) + distribute(root.right)      
            self.moves += abs(coins)  
            return coins

        distribute(root)
        return self.moves