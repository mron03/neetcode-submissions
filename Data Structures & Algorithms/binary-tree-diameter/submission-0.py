# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        def search(root):
            if not root:
                return 0, 0

            
            l, l_max = search(root.left)
            r, r_max = search(root.right)

            best_diameter = max([l + r, l_max, r_max])


            return max(l, r) + 1, best_diameter

        
        return search(root)[1]

