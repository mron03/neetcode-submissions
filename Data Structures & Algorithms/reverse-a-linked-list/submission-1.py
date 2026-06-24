# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None
        
        new_head = ListNode(head.val, None)
        
        while head.next:
            head = head.next
            new_head = ListNode(head.val, new_head)

        
        return new_head

