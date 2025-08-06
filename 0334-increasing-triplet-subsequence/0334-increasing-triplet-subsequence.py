class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # has_a= False
        # for i in range(len(nums)):
        #     print("at i",nums[i])
        #     for j in range(1):
        #         print("at i",nums[j])
        #         if nums[j+1]<1:
        #             print("at i",nums[j+1])
        #             # if nums[j+i+1] < len(nums)-1 and nums[j+i] <len(nums)-1:
        #             if nums[i]<nums[j+1]<nums[j+1]:
        #                 has_a =True
        # return has_a\
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # smallest so far
            elif num <= second:
                second = num  # second smallest
            else:
                # Found third number greater than both -> triplet exists
                return True

        return False

        