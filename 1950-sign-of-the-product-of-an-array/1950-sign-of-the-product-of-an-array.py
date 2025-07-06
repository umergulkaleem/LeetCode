class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # def helper(p,l):
        #     if l == len(nums):
        #         return p
        #     p = p*nums[l]
        #     print(p,"p")
        #     return helper(p,l+1) 
        # res = helper(1,0)
        # print(res)
        # if res > 0:
        #         return 1
        # elif res < 0:
        #         return -1
        # else:
        #         return 0
        p = 1
        for i in nums:
            p = p*i
        if p>0:
            return 1
        elif p<0:
            return -1
        else:
            return 0
        