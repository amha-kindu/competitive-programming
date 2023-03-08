# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        if not root:
            return []
        return self.inOrder(root.left)+[root.val]+self.inOrder(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        in_order = self.inOrder(root)
        for i in range(len(in_order)):
            left = in_order[i-1] if i-1>=0 else -float('inf')
            right = in_order[i+1] if i+1<len(in_order) else float('inf')
            if not(left<in_order[i]<=right):
                return False
        return True
        
