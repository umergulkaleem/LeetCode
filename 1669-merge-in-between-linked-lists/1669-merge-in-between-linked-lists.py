# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        # count1 =0 
        # count2 =0

        # curr1 = list1
        # while curr1:
        #     curr1 = curr1.next
        #     count1+=1
            
        # curr2 = list2
        # while curr2:
        #     curr2 = curr2.next
        #     count2+=1

        # print(count1,count2)

        curr = list1
        i = 0
        while i < a-1:
            curr = curr.next
            i+=1
        
        head = curr

        while i <=b:
            curr = curr.next
            i+=1
        head.next = list2


        while list2.next:
            list2 = list2.next
        list2.next = curr
        return list1



        