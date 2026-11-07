# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = 0 
        cnt = k


        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            
            nonlocal cnt, result

            if cnt == 0:
                return
            
            cnt -= 1

            if cnt == 0:
                result = node.val
            else:

                dfs(node.right)

            
        dfs(root)

        return result
            
