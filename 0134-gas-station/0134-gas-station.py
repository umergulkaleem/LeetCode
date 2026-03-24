class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # rem = 0
 
        # for i in range(len(gas)):
        #     left= gas[i]
        #     count = 1
        #     tmp = i
        #     while left>0:
        #         if tmp == len(gas)-1:
        #             tmp = 0
        #         left = left-cost[tmp]+gas[tmp+1]
        #         tmp+=1
        #         print(left,"at ",i)
        #         count+=1
        #         print(count,"count")
        #         if count == len(gas)-1:
        #             return i+1
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0 
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total<0:
                total = 0
                res= i+1
        return res


            