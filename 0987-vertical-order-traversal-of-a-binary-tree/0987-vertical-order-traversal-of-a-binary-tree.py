# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root, x=0, y=0):
        if not root:
            return
        self.vertical_order[x].append((y, root.val))

        self.verticalOrder(root.left, x-1, y+1)
        self.verticalOrder(root.right, x+1, y+1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.vertical_order = defaultdict(lambda: [])
        self.verticalOrder(root)

        answer = []
        for key in sorted(self.vertical_order.keys()):
            answer.append([val for _, val in sorted(self.vertical_order[key])])
        return answer