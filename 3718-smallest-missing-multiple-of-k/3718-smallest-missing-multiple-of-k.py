class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        check = set(nums)
        # if k > max(nums):
        #     return k
        # for i in range(1,max(nums)):

        #     print(i)
        #     if i not in check and i % k == 0:
        #         return i
        # return max(nums)+k

        multiple = k

        while multiple in check:
            multiple+=k
        return multiple





        