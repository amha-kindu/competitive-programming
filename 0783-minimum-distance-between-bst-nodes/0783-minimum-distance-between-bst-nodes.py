# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseBST(self, root):
        if not root:
            return
        
        self.nums.append(root.val)
            
        self.traverseBST(root.left)
        self.traverseBST(root.right)
        
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        self.traverseBST(root)
        self.nums.sort()
        min_diff = float('inf')
        for i in range(len(self.nums)-1):
            diff = self.nums[i+1] - self.nums[i]
            min_diff = min(min_diff, diff)
        return min_diff