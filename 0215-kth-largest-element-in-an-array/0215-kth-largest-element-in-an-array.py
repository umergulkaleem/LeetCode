class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort1 = sorted(nums)
        # kth = 0
        # print(sort1)
        # for i in range(k):
        #     print(i)
        #     kth = sort1[len(nums)-k]
        # return kth
    
        import heapq

        minheap = []
        for num in nums:
            heapq.heappush(minheap,num)
            # print(num,"num")
            # print(minheap,"minheap")
            if len(minheap)>k:
                heapq.heappop(minheap)
        return minheap[0]


        