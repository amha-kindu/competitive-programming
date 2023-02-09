# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTrav(self, root):
        if not root:
            return
        
        self.postorderTrav(root.left)
        self.postorderTrav(root.right)
        self.postorder.append(root.val)
        
        return
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder = []
        self.postorderTrav(root)
        return self.postorder
        