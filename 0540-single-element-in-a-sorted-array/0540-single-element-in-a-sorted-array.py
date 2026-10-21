class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        even = True
        while l<r:
            mid = (l+r)//2
            if mid % 2 == 0:
                # print(mid % 2)
                # even = True
                other = nums[mid+1]
                # print(nums[mid],other)
                if nums[mid]  != other:
                    # return nums[mid]
                    r = mid
                else:
                    l = mid+2
            else:
                # even = False
                other = nums[mid-1]
                if nums[mid]  != other:
                    
                    r = mid-1
                else:
                    l = mid+1
        return nums[l]
            


            


        