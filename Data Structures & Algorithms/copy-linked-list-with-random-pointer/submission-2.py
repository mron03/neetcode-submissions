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

            
        copy_head = Node(head.val)
        cur_copy_head = copy_head
        hashmap = {head: copy_head}

        cur = head.next
        while cur:
            copy = Node(cur.val)
            cur_copy_head.next = copy
            cur_copy_head = copy
            hashmap[cur] = copy
            cur = cur.next


        cur = head
        while cur:
            random_node = cur.random
            if not random_node:
                cur = cur.next
                continue

            copy_cur = hashmap[cur]
            copy_random = hashmap[random_node]

            copy_cur.random = copy_random
            
            cur = cur.next
        
        return copy_head


