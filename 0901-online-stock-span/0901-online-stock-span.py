class StockSpanner:

    def __init__(self):
        self.days = []

    def next(self, price: int) -> int:
        # count = 1
        # tmp = 0
        # # print(self.days)
        # while tmp<len(self.days) and self.days[-1-tmp]<=price:
        #     # print(self.days[-1+tmp],"at",price)
        #     count+=1
        #     tmp+=1
        # self.days.append(price)
        # return count 

        span = 1 

        while self.days and self.days[-1][0] <= price:
            span+=self.days.pop()[1]
        self.days.append([price,span])

        return span



        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)