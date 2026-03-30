class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        prev = intervals[0]
        for i in range(1,len(intervals)):
            next1 = intervals[i]
            if prev[1]>=next1[0]:
                prev = [min(prev[0],next1[0]),max(prev[1],next1[1])]
            else:
                # print(prev,"p")
                # print(next1,"next")
                res.append(prev)
                prev = next1
                # print(res)
        res.append(prev)
        return res