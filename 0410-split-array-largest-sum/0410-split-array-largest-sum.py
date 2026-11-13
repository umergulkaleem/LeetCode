class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def check(n):
            count = 0
            tmp = 0
            for i in nums:
                tmp+=i
                if tmp>n:
                    tmp = i
                    count+=1
                # if count+1<=k:
                #     return True
                # print(tmp,"tmp")
                # print(count,"cout")
            return count+1<=k

        l,r = max(nums),sum(nums)
        res = 0
        while l<=r:
            m = l+((r-l)//2)
            # print(m)
            if check(m):
                # print("in")
                r=m-1
                res = m
            else:
                l = m+1
        return res

                
        