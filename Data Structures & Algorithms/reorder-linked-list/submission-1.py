# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next
        
        while f and f.next:
            s = s.next
            f = f.next.next

        l1 = head
        l2 = s.next
        s.next = None

        #reverse l2
        prev = None
        curr = l2

        while curr is not None:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        
        l2 = prev
        res_ll = l1

        #reorder
        while l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next
            
            l1 = l1_next
            l2 = l2_next

        return