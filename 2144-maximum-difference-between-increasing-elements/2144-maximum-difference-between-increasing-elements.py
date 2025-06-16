class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # maxdifference =-1
        # maxnum = max(nums)
        # print(maxnum,"maxnum")
        # for i in range(len(nums)):
        #     print(i,"i")
        #     curr = nums[i]
        #     if curr ==max:
        #         return maxdiffernce
        #     print(curr,"curr")
        #     for j in range(i+1,len(nums)):
        #         if i<j:
        #             print(j,)
        #             nextnum = nums[j]
        #             print(nextnum,"nextnum")
        #             if nextnum-curr>maxdifference:
        #                     maxdifference = nextnum-curr
        #                     print(maxdifference,"diff")
        #         else:
        #             maxdifference = -1
                    
                
        # return maxdifference\

        min_val = nums[0]
        max_diff = -1
        
        for i in range(1, len(nums)):
            if nums[i] > min_val:
                max_diff = max(max_diff, nums[i] - min_val)
            else:
                min_val = nums[i]
                
        return max_diff


        