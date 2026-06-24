# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low = min(p.val,q.val)
        high = max(p.val,q.val)

        while True:
            if root.val > low and root.val > high:
                root = root.left
                continue
            elif root.val < low and root.val < low:
                root = root.right
                continue

            return root