# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelTraverse(self, root, depth=0, i=0):
        if not root:
            return

        self.levels[depth]['max'] = max(self.levels[depth]['max'], i)
        self.levels[depth]['min'] = min(self.levels[depth]['min'], i)

        self.levelTraverse(root.left, depth+1, 2*i+1)
        self.levelTraverse(root.right, depth+1, 2*i+2)

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.levels = defaultdict(lambda: {'max': 0, 'min': float('inf')})
        self.levelTraverse(root)

        max_width = 0
        for key in self.levels:
            max_width = max(max_width, self.levels[key]['max']-self.levels[key]['min']+1)
        return max_width
