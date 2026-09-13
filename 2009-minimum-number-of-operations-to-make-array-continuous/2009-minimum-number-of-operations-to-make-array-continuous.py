class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # first check if they are unique and no duplicate
        # every array can be made
        # 
        # dif = max(nums)-min(nums)
        # if (dif == len(nums)-1) and (len(set(nums)) == len(nums)):
        #     return 0
         
        # change =True

        # if dif<len(nums):
        #     change =  False

        # nums.sort()
        # check = set(nums)
        # change = 0
        # print(nums)
        # for i in range(len(nums)-1):
        #     if nums[i]+1 not in check:
        #         change+=1

        # return change        


        n = len(nums)
        nums = sorted(set(nums))
        res = n
        r= 0
        for l in range(len(nums)):

            while r<len(nums) and nums[r] < nums[l]+n:
                r+=1
            win = r-l
            res = min(res,n-win)
        return res


        
        