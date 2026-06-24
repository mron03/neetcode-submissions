# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def search(root):
            nonlocal res

            if not root:
                return 0
            
            l = search(root.left)
            r = search(root.right)

            res = max(l + r, res)

            return max(l, r) + 1

        
        search(root)
        
        return res

