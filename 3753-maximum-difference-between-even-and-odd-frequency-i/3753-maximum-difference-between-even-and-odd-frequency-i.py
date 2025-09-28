class Solution:
    def maxDifference(self, s: str) -> int:
        # max1 = 0
        # max2 = 0
        # freq = Counter(s)
        # print(freq)
        # for i in freq.values():
        #     if i % 2 !=0:
        #         max1 = max(max1,i)
        #     else:
        #         max2 = max(max2,i)
        # print(max1)
        # print(max2)

        # if max1 ==0 or max2 ==0:
        #     return -1
        # return max1-max2
        
        freq = Counter(s)
        odds = [v for v in freq.values() if v % 2 == 1]
        evens = [v for v in freq.values() if v % 2 == 0]

        if not odds or not evens:
            return -1   # no valid (odd, even) pair

        return max(odds) - min(evens)


        