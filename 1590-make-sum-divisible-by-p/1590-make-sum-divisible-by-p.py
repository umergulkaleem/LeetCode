class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        remain =sum(nums)%p

        if remain == 0:
            return 0

        hashmap = {0:-1}

        res = len(nums)
        curr_sum = 0

        for i,n in enumerate(nums):
            curr_sum = (curr_sum+n)%p

            prefix  = (curr_sum-remain+p)%p

            if prefix in hashmap:
                length = i-hashmap[prefix]
                res = min(length,res)
            hashmap[curr_sum] = i

        return -1 if res == len(nums) else res

    