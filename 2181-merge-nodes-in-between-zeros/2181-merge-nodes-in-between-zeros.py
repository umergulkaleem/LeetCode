# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:

        # zero_came = False

        # curr = head

        # total = 0

        # while curr:
        #     if zero_came:
        #         total+=curr.val
        #     if curr.val  == 0 and not zero_came :
        #         zero_came = True
        #     if curr.val  == 0 and zero_came :
        #         tmp = curr.next

                
        #         zero_came = False

        curr = head

        while curr.next:

            node = curr.next
            curr = curr.next

            while curr.next.val  !=0:
                node.val+=curr.next.val
                curr = curr.next
            curr = curr.next
            node.next = curr.next

        return head.next
            
        