# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSumCount(self, root, target, prefixCount, running_sum=0):

        if not root:
            return

        running_sum += root.val
        if (running_sum - target) in prefixCount:
            self.count += prefixCount[running_sum - target]

        prefixCount[running_sum] += 1
        
        self.pathSumCount(root.left, target, prefixCount, running_sum )
        self.pathSumCount(root.right, target, prefixCount, running_sum)

        prefixCount[running_sum] -= 1


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        self.pathSumCount(root, targetSum, defaultdict(int, {0: 1}))

        return self.count
