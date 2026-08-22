class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumofall = 0
        product = 1
        tmp = n
        while tmp>0:
            curr = tmp%10
            # print(curr)
            sumofall+=curr
            product*=curr
            tmp = tmp//10
        # print(sumofall,product)
        
        total = sumofall+product
        return n%total  == 0
        