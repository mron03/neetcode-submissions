# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            prev = None
            curr = head
            stop = tail.next
            while curr != stop:   # stops BEFORE tail.next, so tail IS included ✓
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev  # new head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            count = 0
            while count < k and kth.next:
                kth = kth.next
                count += 1
            if count < k:
                break

            group_head = group_prev.next
            next_group = kth.next          # save BEFORE reverse touches anything

            new_head = reverse(group_head, kth)

            group_prev.next = new_head
            group_head.next = next_group   # use saved pointer
            group_prev = group_head

        return dummy.next