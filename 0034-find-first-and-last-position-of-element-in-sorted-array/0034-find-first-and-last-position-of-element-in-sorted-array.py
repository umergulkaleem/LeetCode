class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left,right = 0 ,len(nums)-1
        # left,right = 0 ,len(nums)-1
        # while left<right:
        #     mid = (left+right)//2
        #     print(f"{mid} at {left}, {right}")
        #     if nums[left] == target and nums[right]==target:
        #         if abs(left-right)>1:

        #             tmp = []
        #             for i in range(left,right):
        #                 tmp.append(i)
        #             return tmp
        #         else:
        #             return[left,right]
        #     elif nums[mid]== target and nums[left] !=target:
        #         left = mid
        #     elif nums[mid]== target and nums[right] !=mid:
        #         right = mid
        #     elif nums[mid]<target  :
        #         left = mid+1
        #     else:
        #         right = mid-1
        # return [-1,-1]
        
        left,right = 0 ,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] <target:
                left  = mid+1
            elif nums[mid]>target:
                right = mid -1
            else:
                l,r= mid,mid
                while l-1>=0 and nums[l-1] == target:
                    l-=1
                while r+1<len(nums) and nums[r+1] == target:
                    r+=1
                return [l,r]
        return[-1,-1]