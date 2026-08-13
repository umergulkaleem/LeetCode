class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
            

        def helper(x):
            if x<0:return 0
            res = 0
            subarray = 0
            l = 0
            for r in range(len(nums)):
                subarray+=nums[r]

                while subarray>x:

                    subarray-=nums[l]
                    l+=1
                res += (r-l+1)
            return res

        return helper(goal)-helper(goal-1)


        