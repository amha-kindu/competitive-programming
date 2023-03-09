# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        if not root:
            return []
        return self.inOrder(root.left)+[root.val]+self.inOrder(root.right)

    def findMode(self, root: Optional[TreeNode], count=defaultdict(int)) -> List[int]:
        in_order = self.inOrder(root)
        count = Counter(in_order)
        multimodes = []
        temp = count.most_common(1)[0][1] 
        for ele in in_order:
            if in_order.count(ele) == temp:
                multimodes.append(ele)
        return list(set(multimodes))
        