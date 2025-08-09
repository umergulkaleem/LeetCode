class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        def helper(n):
            print(n)
            if n == 1:
                return True
            if n < 1 or n % 2 != 0:
                return False
    
                # Recursive call dividing n by 2
            return helper(n // 2)
        return helper(n)