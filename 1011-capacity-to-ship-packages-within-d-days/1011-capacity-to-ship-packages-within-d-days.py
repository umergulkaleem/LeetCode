class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def check(num):
            # print("this is the number",num)
            left = days-1
            new = 0
            for i in weights:
                new+=i
                if new>num:
                    left-=1
                    if left>=0:
                        new =i
                    else:
                        return False
                # print(new,"at",i)
                # print("this is left",left)
            return True
        res = float("inf")
        l,r = max(weights),sum(weights)

        while l<=r:
            mid = l+(r-l)//2
            if check(mid):
                # print(check(mid),"this came")
                res = min(res,mid)
                r = mid-1
            else:
                l = mid+1
        return res




                    