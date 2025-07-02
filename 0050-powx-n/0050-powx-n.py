class Solution:
    def myPow(self, x: float, n: int) -> float:
        # count=0
        # ans = 1
        # def helper(x,n,count,ans):
        #     if n>0:
        #         print(n)
        #         print(count)
        #         if count == n:
        #             return ans
        #         ans = ans*x
        #         print(type(ans))
        #         return helper(x,n,count+1,ans)
        #     elif n<0:
        #         print(int(n))
        #         print(count)
        #         if count == int(n):
        #             return ans
        #         ans = ans/x
        #         print(type(ans))
        #         return helper(x,n,count-1,ans)

        # return helper(x,n,count,ans)
        def helper(x, n):
            if n == 0:
                return 1
            half = helper(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n
        return helper(x, n)

