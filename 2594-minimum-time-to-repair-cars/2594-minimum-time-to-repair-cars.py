class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """
        i think the fastest to all the car is the max time we opt from there



        """

        def check(mint):
            count = 0
            # print("the min is",mint)
            for r in ranks:

                count+=int((mint//r)**0.5)
                # print(count,"at rank",r)
            if count>=cars:
                return True
            else:
                return False


        l,r = 0,min(ranks)*cars**2
        res = 0
        while l<=r:

            mid = l+((r-l))//2

            if check(mid):
                r = mid-1
                res = mid
            else:
                l = mid+1
        return res


        