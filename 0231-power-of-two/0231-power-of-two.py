class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def helper(n,i):
            print(i)
            if 2**i == n:
                print("in True")
                return True
            if i>=31:
                print("in false")
                return False
            return helper(n,i+1)

        return helper(n,0)
            
    

        