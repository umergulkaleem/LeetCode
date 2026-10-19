class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        

        # if len(nums) == 1 and nums[0] == target:
        #     return nums
            
        # nums.sort()
        # first_instance = 0
        # result =[]
        # l,r = 0,len(nums)-1

        # while l<=r:

        #     mid = (l+r)//2
        #     # print(nums[mid])
        #     if nums[mid]==target:
        #         first_instance = mid
        #         r= mid-1
        #     elif nums[mid]>target:
        #         r = mid-1
        #     else:
        #         l = mid+1

        # # print(nums,"list")
        # # print(first_instance,"fi")
        # while first_instance<len(nums) and nums[first_instance] == target:
        #     result.append(first_instance)
        #     first_instance +=1
        # # while first_instance >=0 and nums[first_instance] == target:
        # #     result.insert(0,first_instance)
        # #     first_instance-=1
        # #     # print(first_instance,"fi")
        # return result


        instances = 0
        smaller = 0

        for n in nums:
            if n == target:
                instances+=1
            elif n<target:
                smaller+=1
        
        result = []
        for n in range(instances):
            result.append(smaller)
            smaller+=1
        return result


        