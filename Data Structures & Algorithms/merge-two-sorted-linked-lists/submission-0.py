# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

            
        if list1.val < list2.val:
            new_head = ListNode(list1.val)
            list1 = list1.next
        else:
            new_head = ListNode(list2.val)
            list2 = list2.next

        res = new_head


        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    new_head.next = list1
                    new_head = new_head.next
                    list1 = list1.next
                else:
                    new_head.next = list2
                    new_head = new_head.next
                    list2 = list2.next
            elif list1:
                new_head.next = list1
                new_head = new_head.next
                list1 = list1.next
            elif list2:
                new_head.next = list2
                new_head = new_head.next
                list2 = list2.next


        return res

                    