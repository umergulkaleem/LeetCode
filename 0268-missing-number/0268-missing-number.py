class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j] = nums[j],nums[i]
        # # return nums
        # no = nums[0]
        # for i in nums:
        #     if i !=no:
        #         return no
        #     no+=1
        appear = set()
        for i in nums:
            appear.add(i)
        
        n = 0
        while n<=len(nums):
            if n not in appear:
                return n
            n+=1

            
            
        