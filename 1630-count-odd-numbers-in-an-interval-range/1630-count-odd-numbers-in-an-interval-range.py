class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # oddofhigh = high/2 +1
        # print(oddofhigh)
        # oddoflow = low/2
        # print(oddoflow)
        odd = (high+1)/2 - (low/2)
        # return int(oddofhigh - oddoflow)
        if high%2==0 or low %2 ==0:
            return int(odd)
        else:
            return int(odd+1)
            