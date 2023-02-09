# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTrav(self, root):
        if not root:
            return
        self.inorderTrav(root.left)
        self.inorder.append(root.val)
        self.inorderTrav(root.right)
        
        return
    
    def inorderTraversal(self, root: Optional[TreeNode], inorder=[]) -> List[int]:
        self.inorder = []
        self.inorderTrav(root)
        return self.inorder
        