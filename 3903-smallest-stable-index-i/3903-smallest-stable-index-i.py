class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        tmin = min(nums)
        tmax = max(nums)
        # res = float("-inf")
        tmp = 0
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     if curr>tmax:
        #         tmax = curr
        #     if curr <tmin:
        #         tmin = curr
        #     print(tmax,tmin)
        #     res = min(res,tmax-tmin)
        #     print(res)
        count = 0
        while count<len(nums):
            left = nums[:count+1]
            right = nums[count:]
            tmax = max(left)
            tmin = min(right)
            if  tmax-tmin<=k:
                return count

            print(left,tmax,right,tmin)
            count+=1
        return -1

        