# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPaths(self, root, path=''):
        if not root:
            return 
        if not root.left and not root.right:
            self.all_paths.append(path+f'{root.val}')

        self.getPaths(root.left, path+f'{root.val}->')
        self.getPaths(root.right, path+f'{root.val}->')

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.all_paths = []
        self.getPaths(root)
        return self.all_paths
