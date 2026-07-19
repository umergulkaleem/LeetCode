class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_sum  = sum(nums)
        window = 0
        l = 0
        res = float("inf")
        for r in range(len(nums)):
            # if l == r :
            #     window=nums[l]
            # else:
            #     window = sum(nums[l:r+1])
            # print("at",l,r ,"window is",window)
            # if window >= target:
            #     print("in")
            #     res = min(r+l+1,res)
            window +=nums[r]
            
            while window >= target:
                window -=nums[l]
                res = min(r-l+1,res)
                l+=1
        return res if res != float(inf) else 0


        