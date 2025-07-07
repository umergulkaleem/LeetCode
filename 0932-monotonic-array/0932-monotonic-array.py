class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # if nums[0]<nums[1]:
        #     method = "inc"
        # else:
        #     method = "dec"
        # for i in range(len(nums)):
            # print(i,"i")
            # curr = nums[i]
            # if i <len(nums)-1:
            #     nex= nums[i+1]
            #     diff = curr-nex
            #     print(diff)
            #     if diff not in (1, -1, 0):
            #         return False
            # if method == "inc":
            #     print("in inc")
            #     curr = nums[i]
            #     if i <len(nums)-1:
            #         nex= nums[i+1]
            #         if nex<curr:
            #             return False
            # elif method == "dec":
            #     print("in dec")
            #     curr = nums[i]
            #     if i <len(nums)-1:
            #         nex= nums[i+1]
            #         if nex>curr:
            #             return False
            # return True

            increasing = decreasing = True
            if len(nums) == 1:
                return True

            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    decreasing = False
                if nums[i] < nums[i - 1]:
                    increasing = False

            return increasing or decreasing

        # return True

        