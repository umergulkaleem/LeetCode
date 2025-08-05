class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sums = []
        # for i in range(len(nums)):
        #     product =1 
        #     for k in range(len(nums)):
        #         if i!=k:
        #             product = product*nums[k]
        #             print(product,"at ",nums[k],"at",nums[i])
                    
        #     sums.append(product)
        # return sums
        n = len(nums)
        result = [1]*n

        prefix = 1
        for i in range(n):
            result[i]=prefix
            prefix *=nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            result[i]*=suffix
            suffix *=nums[i]
                    
        return result
            


        