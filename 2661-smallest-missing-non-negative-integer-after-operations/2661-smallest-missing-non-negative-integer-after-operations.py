class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter([num % value for num in nums])

        mex = 0
        while True:
            r = mex % value
        
            if count[r] > 0:
                
                count[r] -= 1
                
                mex += 1
            else:
                return mex
        