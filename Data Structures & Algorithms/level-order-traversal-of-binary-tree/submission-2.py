# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = [root]


        while queue:
            temp = []
            next_queue = []

            for q in queue:
                temp.append(q.val)
                if q.left:
                    next_queue.append(q.left)

                if q.right:
                    next_queue.append(q.right)
            
            result.append(temp)
            queue = next_queue

        return result

