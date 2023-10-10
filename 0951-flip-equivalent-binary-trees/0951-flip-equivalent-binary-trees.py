# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (root1 == None) or (root2 == None):
            return not root1 and not root2
        
        if root1.val != root2.val:
            return False
            
        root1_left = root1.left.val if root1.left else float('inf')
        root2_left = root2.left.val if root2.left else float('inf')

        root1_right = root1.right.val if root1.right else float('inf')
        root2_right = root2.right.val if root2.right else float('inf')

        if root1_left == root2_right and root1_right == root2_left:
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        else:
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)



        
        