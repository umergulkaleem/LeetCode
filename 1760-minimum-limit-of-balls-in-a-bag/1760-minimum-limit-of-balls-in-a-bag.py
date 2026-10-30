class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:

        """
        one till the max in the nums array

        """
        
        def check(max_balls):
            op = 0
            for n in nums:
                op+=ceil(n/max_balls)-1
                if op>maxOperations:
                    return False
            return True

        l,r =1 ,max(nums)
        res = r
        while l<r:
            mid = l+((r-l)//2)

            if check(mid):
                r = mid
                res = mid
            else:
                l = mid+1
        return res