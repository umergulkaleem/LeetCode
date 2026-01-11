# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # point1 = head 
        # point2 = head.next
        # length = 1
        # while point2.next:
        #     point2 = point2.next
        #     length+=1
        # length+=1
        # # print(point1.val)
        # # print(point2.val)
        # # print(length)
        # count = 0
        # while point1<point2:
        #     temp = point1.next
        #     point1.next  = point2
        #     point2.next = temp
        #     point2 -=1
        #     point1+=1
        #     print(head)
        slow = head
        fast = head.next
        length = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length+=2
        prev = None
        curr = slow.next
        slow.next = None   
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        point1 = head
        point2 = prev
        while point2:
            temp1,temp2= point1.next,point2.next
            point1.next = point2
            point2.next = temp1
            point1 = temp1
            point2 = temp2


            


