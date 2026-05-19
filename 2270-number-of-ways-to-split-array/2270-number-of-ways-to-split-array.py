class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid = 0

        total = sum(nums)   
        left ,right= 0,total
        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]
            if left>=right:
                valid+=1
            
        return valid
        