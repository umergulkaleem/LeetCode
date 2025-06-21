class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # def helper(n,i):
        #     if 4**i == n:
        #         return True 
        #     if i>=31:
        #         return False
        #     return helper(n,i+1)
        # return helper(n,0)
        def helper(x):
            print(x)
            if x == 1:
                return True
            if x % 4 != 0 or x == 0:
                return False
            return helper(x//4)
        return helper(n)
        