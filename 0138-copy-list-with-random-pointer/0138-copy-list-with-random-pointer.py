"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldHashmap = {None:None}
        curr =head
        while curr:
            copy = Node(curr.val)
            oldHashmap[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldHashmap[curr]
            copy.next = oldHashmap[curr.next]
            copy.random = oldHashmap[curr.random]
            curr = curr.next
        return oldHashmap[head]