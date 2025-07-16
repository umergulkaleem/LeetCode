# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =temp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val +=l1.val
                l1 = l1.next
            if l2:
                sum_val +=l2.val
                l2 = l2.next
            carry,fly = divmod(sum_val,10)
            temp.next = ListNode(fly)
            temp = temp.next
        return dummy.next
    