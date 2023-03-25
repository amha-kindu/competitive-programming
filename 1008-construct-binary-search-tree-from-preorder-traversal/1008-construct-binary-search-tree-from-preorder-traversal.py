# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int], left=0, right=0) -> Optional[TreeNode]:
        n = len(preorder)

        if left==0 and right==0:
            right = n-1

        if left > right:
            return

        new_node = TreeNode(preorder[left])
        next_smaller, next_bigger_eq = n, n
        for j in range(left+1, n):
            if preorder[j] < preorder[left]:
                next_smaller = j
            else:
                next_bigger_eq = j
                break

        new_node.left = self.bstFromPreorder(preorder, left=left+1, right=next_bigger_eq-1)
        new_node.right = self.bstFromPreorder(preorder, left=next_bigger_eq, right=right)

        return new_node
        