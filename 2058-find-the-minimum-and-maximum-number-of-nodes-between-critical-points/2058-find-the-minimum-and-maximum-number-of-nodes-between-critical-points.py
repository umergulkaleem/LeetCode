# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev= head

        curr = head.next

        nextnode = curr.next
        # ans = []
        idx = 1
        index = []
        while curr.next:

            if curr.val>prev.val and curr.val>nextnode.val:
                # ans.append(curr.val)
                index.append(idx)
            if curr.val<prev.val and curr.val<nextnode.val:
                index.append(idx)
                # ans.append(curr.val)
        
                # ans.append(-1)
            idx +=1
            prev = curr
            curr = nextnode
            nextnode = nextnode.next
        # print(ans)
 
        if len(index)<2:
            return [-1,-1]
        mindistance = float("inf")

        for i in range(1,len(index)):
            mindistance = min(mindistance,index[i]-index[i-1])
        
        maxdistance = index[-1]-index[0]
        return [mindistance,maxdistance]

        