# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        prev = None
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        prev.next = slow_ptr.next
        return head
        