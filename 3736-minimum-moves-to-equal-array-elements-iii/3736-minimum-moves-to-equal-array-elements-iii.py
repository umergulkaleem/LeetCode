class Solution:
    def minMoves(self, nums: List[int]) -> int:

        count = 0
        maximum = max(nums)
   

        for n in nums:
            count+=maximum-n
        
        return count 

        