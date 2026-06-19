class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingTime = 0
        total = 0
        for i , j in customers:
            if waitingTime>i:
                total += waitingTime-i
            else:
                waitingTime = i
            total += j
            waitingTime+=j

            

        return total/len(customers)