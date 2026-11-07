# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root, low, high):
        if not root:
            return True

        if low < root.val < high:
            return (
                self.dfs(root.left, low, root.val) and
                self.dfs(root.right, root.val, high)
            )
        
        return False

        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None

        result = self.dfs(root, float('-inf'), float('inf'))

        return result