class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        arr1 = [0]*len(nums)
        tmp = 0
        for i in range(len(nums)-1,-1,-1):
            # print(i)
            tmp = max(tmp,nums[i])
            arr1[i] = tmp
        print(arr1)

        l = 0
        res = 0
        for r in range(len(nums)):
         
            while l<len(nums) and l<r and nums[l]>arr1[r]:
                l+=1
                
            res= max(res,r-l)

        return res

