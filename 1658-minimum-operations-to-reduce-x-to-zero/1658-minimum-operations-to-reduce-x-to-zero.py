class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # res = -1

        # l,r = 0,len(nums)-1

        # while l!=r:
        #     if nums[l]>nums[r] and nums[l]<k:
        #         curr+=num[l]

        #     if curr == x:
        #         res = min(res,curr)
        
        res = -1
        target = sum(nums)-x
        if target<0:
            return -1
        if target == 0:
            return len(nums)
        
        l = 0
        window  = 0
        # print(target,window)
        for r in range(len(nums)):
            window+=nums[r]
            # print(window,"outloop")
            while window>target:
                window-=nums[l]
                # print(window,"inloop")
                l+=1
            if target == window:
                res = max((r-l+1),res)
        return -1 if res == -1 else len(nums)-res
