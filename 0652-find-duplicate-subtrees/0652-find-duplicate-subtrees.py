# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = defaultdict(set)
        subtrees = set()
        def traverse(node):
            nonlocal ans, subtrees
            if not node:
                return None
            left = traverse(node.left)
            right = traverse(node.right)
            curr =  str(node.val) + "," + str(left) + "," + str(right)
            if curr in subtrees and curr not in ans:
                ans[curr].add(node)
            subtrees.add(curr)
            return curr
        traverse(root)
        return [ x.pop() for x in ans.values() if x]

        