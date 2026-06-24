class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        node = head
        while node:
            lst.append(node)
            node = node.next

        i, j = 0, len(lst) - 1
        while i < j:
            lst[i].next = lst[j]   # 0 → n-1
            if i + 1 < j:
                lst[j].next = lst[i + 1]  # n-1 → 1
            i += 1
            j -= 1

        lst[i].next = None  # ← critical: terminate the middle node