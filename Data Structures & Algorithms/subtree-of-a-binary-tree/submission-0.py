# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def check_similarity(original, to_check):
            if (not original and to_check) or (not to_check and original):
                return False
            
            if not original and not to_check:
                return True
            
            if original.val != to_check.val:
                return False
            
            return check_similarity(original.left, to_check.left) and check_similarity(original.right, to_check.right)

        def full_check(root, subRoot):
            if not root or not subRoot:
                return False
            
            if check_similarity(root, subRoot):
                return True

            return full_check(root.left, subRoot) or full_check(root.right, subRoot)

        return full_check(root, subRoot)