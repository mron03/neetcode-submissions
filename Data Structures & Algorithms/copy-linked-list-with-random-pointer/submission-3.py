"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        cur = head
        old_to_new = {}

        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        

        cur = head
        while cur:
            copy = old_to_new.get(cur)
            next = old_to_new.get(cur.next)
            random = old_to_new.get(cur.random)
            copy.next = next
            copy.random = random
            cur = cur.next

        return old_to_new[head]





