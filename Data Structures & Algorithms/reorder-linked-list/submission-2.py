# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverselist(self, head):
        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        t, h = head, head.next
        while h and h.next:
            t = t.next
            h = h.next.next
        
        tail = self.reverselist(t.next)
        t.next = None

        while head or tail:
            temp = head.next
            head.next = tail
            head = temp
            
            if tail:
                temp = tail.next
                tail.next = head
                tail = temp
        















