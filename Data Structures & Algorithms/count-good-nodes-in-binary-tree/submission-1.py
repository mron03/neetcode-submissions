# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m):
            if not root:
                return 0
            
            l = dfs(root.left, max(m, root.val))
            r = dfs(root.right,max(m, root.val))

            if root.val < m:
                return l + r
            else:
                return l + r + 1


        return dfs(root, float('-inf'))
