class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # prevmax=0
        # max1 = 0
        # for i in range(len(nums)):
        #     currmax= 0
        #     print(i,"i")
        #     currmax+=nums[i]
        #     for j in range(len(nums)):
        #         print(j,"j")
        #         if i !=j:
                    
        #             currmax+=nums[j]
        #         print(currmax,"currmax")
        #     print(prevmax,"prevmax")
        #     max1 = max(currmax,prevmax)
        #     currmax = prevmax
        # return max1


        # kadane algorithm
        
        max_sum = curr_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
