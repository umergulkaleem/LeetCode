class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-x for x in nums]
        heapq.heapify(maxheap)

        for i in range(k):
            res = heapq.heappop(maxheap)
        return -res
        