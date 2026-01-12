# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        point1 = head
        point2 = head
        for i in range(n):
                point2 = point2.next
        if not point2:
            return head.next
        while point2.next:
            point1 = point1.next
            point2 = point2.next
            
        
        point1.next = point1.next.next
        return head

        
