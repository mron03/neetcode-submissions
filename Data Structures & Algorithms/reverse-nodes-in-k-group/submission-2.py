class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, stop):
            prev = None
            curr = head
            while curr != stop:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        dummy = head
        count = 0
        prev_tail = None
        result = None

        while dummy:
            count += 1
            if count == k:
                tail = dummy
                next_group = dummy.next
                new_head = reverse(head, next_group)

                if not result:
                    result = new_head
                if prev_tail:
                    prev_tail.next = new_head
                prev_tail = head

                dummy = next_group
                head = next_group
                count = 0
                continue

            dummy = dummy.next

        # stitch remaining nodes (less than k) to the last reversed group's tail
        if prev_tail:
            prev_tail.next = head

        return result