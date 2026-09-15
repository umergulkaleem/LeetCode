class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # arr = []
        # new = []

        # curr  =float("inf")
        # last = nums[-1][-1]
        # while curr != last and nums:

        #     from_arr_remove = 0
        #     for i in range(len(nums)):
        #         # print(curr,nums[i][0],"curr and now")
        #         if curr>nums[i][0]:
        #             from_arr_remove = i
        #             curr = nums[i][0]
        #     nums[from_arr_remove].pop(0)
        #     if len(nums[from_arr_remove]) == 0:
        #         nums.pop(from_arr_remove)
        #     # print(nums)
        #     arr.append(curr)
        #     curr  =float("inf")

        # print(arr)

        k = len(nums)
        min_heap = []
        left = right = nums[0][0]
        
        for i in range(k):
            curr = nums[i]
            left = min(left,curr[0])
            right = max(right,curr[0])

            heapq.heappush(min_heap,(curr[0],i,0))#curr element , in which arr,index
        
        res = [left,right]

        while True:
            curr,i,idx = heapq.heappop(min_heap)
            idx+=1
            if idx == len(nums[i]):
                return res
            next_val = nums[i][idx]
            heapq.heappush(min_heap,(next_val,i,idx))

            right = max(right,next_val)
            left =min_heap[0][0]
            if right - left < res[1]-res[0]:
                res = [left,right]



        