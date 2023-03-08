# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelTraverse(self, root, depth=0):
        if not root:
            return depth
        self.level_order[depth].append(root.val)

        left_depth = self.levelTraverse(root.left, depth+1)
        right_depth = self.levelTraverse(root.right, depth+1)

        return max(left_depth, right_depth)

    def rightSideView(self, root: Optional[TreeNode], right_view=[]) -> List[int]:
        MAX_DEPTH = 100
        self.level_order = [[] for _ in range(MAX_DEPTH)]

        depth = self.levelTraverse(root)

        return [level[-1] for level in self.level_order[:depth]]
        