# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def func(root, range):
            if not root:
                return True
            
            if root.val <= range[0] or root.val >= range[1]:
                return False
            
            
            range_l = [range[0], root.val]            
            range_r = [root.val, range[1]]      

            return func(root.left, range_l) and func(root.right, range_r)      


        return func(root, [float('-inf'), float('+inf')])