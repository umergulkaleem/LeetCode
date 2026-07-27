class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        print(max1,max2)
        return (max1-1)*(max2-1)
        