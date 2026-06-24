# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True

        def check(p, q):
            if not p and not q:
                return
            
            nonlocal ans
            if (not p and q) or (not q and p) or (p.val != q.val):
                ans = False
                return
            
            check(p.left, q.left)
            check(p.right, q.right)
        

        check(p, q)

        return ans