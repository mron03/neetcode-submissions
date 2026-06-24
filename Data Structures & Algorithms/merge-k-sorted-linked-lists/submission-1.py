# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        dummy = result
        
        while True:
            minimal = -1

            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minimal == -1:
                    minimal = i
                else:
                    if lists[minimal].val > lists[i].val:
                        minimal = i

            if minimal == -1:
                break

            dummy.next = ListNode(lists[minimal].val)
            dummy = dummy.next
            lists[minimal] = lists[minimal].next

        return result.next
