# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)

        
        while queue:
            next_queue = collections.deque()

            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                
                if node.right:
                    next_queue.append(node.right)

            res.append(queue.pop().val)
            
            queue = next_queue 
        
        return res