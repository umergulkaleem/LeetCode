class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainder = {0:-1}
        total = 0

        for i,n in enumerate(nums):
            total+=n
            mod = total%k
            if mod not in remainder:
                remainder[mod] = i

            elif i-remainder[mod]>1:
                return True
        return False
        