class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        # has_a = False
        # at = 0
        # for i in range(len(nums)):
        #     sum1 = 0
        #     sum2 = 0
        #     print(i,"i")
        #     middle = i
        #     # if i>0 and i <len(nums)-1:
        #     for j in range(i,-1,-1):
        #             print(j,"j")
        #             sum1+=nums[j]
        #     for k in range(i,len(nums)):
        #         print(k,"k")
        #         sum2+=nums[k]
        #     print(sum1,"sum1")
        #     print(sum2,"sum2")
        #     if has_a == False:
        #         if sum1 == sum2:
        #             has_a =True
        #             at  = i
        # if  has_a:
        #     return at
        # else:
        #     return -1

        # gpt 
 
        total_sum = sum(nums)       # sum of entire list
        left_sum = 0                # sum from start to i-1

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]     # move to next position

        return -1


        