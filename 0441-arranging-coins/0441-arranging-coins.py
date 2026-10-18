class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1
        while n>count:
            n-=count
            if n>count:
                count+=1
            # print("count",count,n)
        return count