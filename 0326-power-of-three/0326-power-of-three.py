class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n,i):
            if i<=1:
                if i==1 :
                    print("true")
                    return True
                else:
                    print("false")
                    return False
            # i = n/3
            print(i,"in helper")
            return helper(n,i/3)
        i = n
        return helper(n,i)