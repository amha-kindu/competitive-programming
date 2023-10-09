# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPath(self, root, target, path):
        if not root:
            return

        isleaf = not root.left and not root.right

        if isleaf:
            path.append(root.val)
            if sum(path) == target:
                self.solutions.append(path)
            return

        self.findPath(root.left, target, path+[root.val])
        self.findPath(root.right, target, path+[root.val])
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.solutions = []

        self.findPath(root, targetSum, [])

        return self.solutions