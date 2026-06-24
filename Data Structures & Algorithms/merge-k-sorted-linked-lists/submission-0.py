# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = []
        
        for l in lists:
            pointer = ListNode(next=l)
            pointers.append(pointer)

        result = ListNode()
        dummy = result
        while True:
            minimal = None
            continue_loop = False

 

            print("-----")
            for p in pointers:
                if not p.next:
                    continue
                if not minimal:
                    minimal = p
                else:
                    if minimal.next.val > p.next.val:
                        minimal = p

            if not minimal:
                break
                
            print("Minimal", minimal.next.val)
            new_node = ListNode(minimal.next.val)
            dummy.next = new_node
            dummy = new_node

            minimal.next = minimal.next.next
                
            for p in pointers:
                if p:
                    continue_loop = True

            if not continue_loop:
                break

        return result.next
