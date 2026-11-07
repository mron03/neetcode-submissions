# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurse(self, head, n):
        if not head:
            return 0

        k = self.recurse(head.next, n)

        if k == n:
            head.next = head.next.next

        return k + 1

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = self.recurse(head, n)
        if k == n:
            return head.next

        return head

