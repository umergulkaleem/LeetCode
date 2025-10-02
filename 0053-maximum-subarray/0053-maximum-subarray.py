class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        max_sum =0
        for i in range(len(nums)):
            max_sum =max_sum+ nums[i]

            if max_sum>ans:
                ans=max_sum
            if max_sum<0:
                max_sum=0
        return ans        