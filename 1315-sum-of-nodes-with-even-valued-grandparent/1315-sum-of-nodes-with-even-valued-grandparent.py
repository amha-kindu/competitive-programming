# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.even_sum = 0
        def evenGrandparents(node, grand=[]):
            if len(grand) > 2:
                grand.pop(0)

            if not node:
                return
            if len(grand) == 2 and grand[0] % 2 == 0:
                self.even_sum += node.val

            evenGrandparents(node.left, grand+[node.val])
            evenGrandparents(node.right, grand+[node.val])

        evenGrandparents(root)
        return self.even_sum