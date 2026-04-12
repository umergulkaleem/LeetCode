# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        if not curr or not curr.next:
            return head
        curr = head
        newhead = curr.next
        prev = None
        while curr and curr.next:
            on = curr
            nextnode = curr.next
            nexttonext = nextnode.next
            nextnode.next = curr
            if prev:
                prev.next = nextnode
            curr.next = nexttonext
            prev= curr
            curr = nexttonext
        return newhead

        