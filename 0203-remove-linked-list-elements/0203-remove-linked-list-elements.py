# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head == None:
            return head
        print(head.val)
        while head and head.val == val:
            head = head.next
        
        print(head)

        curr = head
        prev = None
        
        while curr:
            print(curr.val)
            if curr.val == val:
                tmp = curr.next
                prev.next = tmp
                curr = curr.next
            else:
                prev= curr
                curr = curr.next
        return head

        