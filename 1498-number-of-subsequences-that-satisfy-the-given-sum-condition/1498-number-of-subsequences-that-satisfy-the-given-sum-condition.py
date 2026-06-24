class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # res = 0
        # p1,p2 = 0,0
        # while p2<len(nums):
        #     first = min(nums[p1:p2+1])
        #     print(first)
        #     second = max(nums[p1:p2+1])
        #     if first + second  <= target:
        #         res+=1

        #     p2+=1
        # return res
        nums.sort()
        res = 0

        r   = len(nums)-1
        mod = (10**9+7)
        for i,left in enumerate(nums):
            while(left+nums[r])> target and i <= r:
                r-=1
            if i<=r:
                res +=(2**(r-i))
                res%=mod
        return res
        