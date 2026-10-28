class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        """
        limit is sum of the quantities

        one type to one store
        min prodcuct quantity to for all hte store
        """ 
        if n == 1:
            return quantities[0]

        def check(m):
            # new = quantities
            if m == 0:
                return False
            i= 0 
            count = 0 
            # print(m,"at this m")
            # while i < len(new):
            #     # print(new)
            #     curr = new[i]
            #     while True:
            #         curr-=m
            #         count+=1
            #         if curr<=0:
            #             break
            #     i+=1
            #     # print("after",count)
            for q in quantities:
                count += (q + m - 1) // m
            if count<=n:
                return True
            else:
                return False
        
        l,r = 0,sum(quantities)
        res = r
        while l<=r:
            m = l+(r-l)//2

            if check(m):
                res = m
                r = m-1
            else:
                l = m+1
        return res

        