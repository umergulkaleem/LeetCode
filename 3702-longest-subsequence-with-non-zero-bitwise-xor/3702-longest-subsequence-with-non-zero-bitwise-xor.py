class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # res = 0
        # l = 0
        # tmp = nums[l]
        # for r in range(1,len(nums)):
        #     tmp = tmp^nums[r]
        #     print(tmp,"l=",nums[l],"r=",nums[r])
        #     while tmp==0:
        #         tmp = tmp^nums[l]
        #         l+=1
        #     res = max(res,r-l+1)
        # return res

        total = 0
        for n in nums:
            total^=n
        if total!=0: return len(nums)

        if any(x!=0 for x in nums):
            return len(nums)-1
        return 0 
        