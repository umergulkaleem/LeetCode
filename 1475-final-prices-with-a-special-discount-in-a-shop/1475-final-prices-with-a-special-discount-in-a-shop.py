class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # arr=  []
        # minimum = prices[-1]
        # arr.append(minimum)
        # for i in range(len(prices)-2,-1,-1):
        #     minimum = min(minimum,prices[i+1])
        #     curr= prices[i]
        #     if minimum<=curr:
        #         arr.append(curr-minimum)
        #     else:
        #         arr.append(curr)
         
        # return arr[::-1]

        arr = []
        stack = []

        for i in range(len(prices)-1,-1,-1):
            curr= prices[i]

            while stack and stack[-1]>curr:
                stack.pop()
            if stack:
                arr.append(curr-stack[-1])
            else:
                arr.append(curr)
            
            stack.append(curr)
        return arr[::-1]