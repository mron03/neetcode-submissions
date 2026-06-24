# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0

        head = ListNode()
        cur = head
        
        while l1 or l2:
            if not l1:
                l1_val = 0
            else:
                l1_val = l1.val
            
            if not l2:
                l2_val = 0
            else:
                l2_val = l2.val

            sum = l1_val + l2_val + remainder

            remainder = 1 if sum >= 10 else 0
                
            cur.next = ListNode(sum % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        if remainder == 1:
            cur.next = ListNode(1)

        return head.next


            

