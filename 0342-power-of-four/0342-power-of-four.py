class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(n,i):
            if 4**i == n:
                return True 
            if i>=31:
                return False
            return helper(n,i+1)
        return helper(n,0)
        