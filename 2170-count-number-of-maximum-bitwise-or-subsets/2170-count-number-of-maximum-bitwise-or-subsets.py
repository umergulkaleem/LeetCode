class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        bitwise = 0
        count = 0
        for i in range(len(nums)):

            bitwise = bitwise|nums[i]
            # print(bitwise)

        def backtrack(index,curror):
            nonlocal count
            if index == len(nums):
                if curror == bitwise:
                    count += 1
                return

            # Safe calls - only if index is in range
            backtrack(index + 1, curror | nums[index])  # Include nums[index]
            backtrack(index + 1, curror) 

        backtrack(0,0)
        return count
                 
        