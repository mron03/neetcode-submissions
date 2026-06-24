# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            low = p.val
            high = q.val
        else:
            low = q.val
            high = p.val

        while True:
            if root.val > high:
                root = root.left
            elif root.val < low:
                root = root.right
            else:
                return root