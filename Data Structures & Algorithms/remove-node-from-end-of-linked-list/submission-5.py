# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        
        if size == 1:
            return None

        target = size - n

        if target == 0:
            return head.next


        temp = head 
    
        for i in range(size - 1):
            if (i + 1) == target:
                temp.next = temp.next.next
                break
            else:
                temp = temp.next
        

        return head



        


            