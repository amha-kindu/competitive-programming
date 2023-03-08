# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateAvg(self, root):
        if not root:
            return 0, 0
        left_sum, left_cnt = self.evaluateAvg(root.left)
        right_sum, right_cnt = self.evaluateAvg(root.right)
        
        tree_sum, tree_cnt = (left_sum + root.val + right_sum),  left_cnt + 1 + right_cnt
        root_avg = tree_sum // tree_cnt

        if root_avg == root.val:
            self.count += 1

        return tree_sum, tree_cnt

        

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.evaluateAvg(root)
        return self.count
        