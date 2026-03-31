class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        total = 0
        intervals.sort()
        prev= intervals[0]
        for i in range(1,len(intervals)):
            next1 = intervals[i]
            if prev[1] > next1[0]:
                total+=1
                prev = [prev[0],min(prev[1],next1[1])]
            else:
                prev = next1
        return total
                 
        