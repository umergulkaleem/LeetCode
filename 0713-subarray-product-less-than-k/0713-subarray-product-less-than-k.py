class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        product = 1 
        res = 0
        l = 0

        for r in range(len(nums)):
            product*=nums[r]
            while l <=r and product>=k:
                product = product//nums[l]
                l+=1
            res+=r-l+1
        return res


        
        product = 1
        res = 0
        total_subset = 1<<n
        print(total_subset)
        # for i in range(total_subset):
        #     sub_product = 1
        #     for j in range(n):
        #         if i &(1<<j):
        #             sub_product*=nums[j]
        #     if sub_product<k:
        #         res+=1
        # return res
        