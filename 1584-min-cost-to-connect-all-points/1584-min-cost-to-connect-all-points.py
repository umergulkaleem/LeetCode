class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1,y1  = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        res= 0
        minh = [[0,0]]
        visit = set()
        while len(visit)<N:
            cost,i = heapq.heappop(minh)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            for neigCost,neig in adj[i]:
                if neig not in visit:
                    heapq.heappush(minh,[neigCost,neig])
        return res


        