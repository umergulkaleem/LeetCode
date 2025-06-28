class Solution:
    def mySqrt(self, x: int) -> int:
        # i = 0
        # while i * i <= x:
        #     i += 1
        # return i - 1
        l =1
        r = x
        while l<=r:
            m = (l+r)//2
            sqr = m*m
            if sqr ==x:
                return m
            elif sqr<x:
                l =m+1
            else:
                r=m-1
        return r

      