# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            next_queue = deque()
            subres = []
            while queue:
                cur = queue.popleft()
                subres.append(cur.val)
                
                if cur.left:
                    next_queue.append(cur.left)
                
                if cur.right:
                    next_queue.append(cur.right)
            
            queue = next_queue
            res.append(subres)

        return res
                
                
    

