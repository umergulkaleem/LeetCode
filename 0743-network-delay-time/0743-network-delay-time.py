class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        #dijkstra algorithm
        for u,v,w in times:
            edges[u].append((v,w))
        minHeap = [(0,k)]
        visit = set()
        t = 0
        while minHeap:
            w,node = heapq.heappop(minHeap)
            if node  in visit:
                continue
            visit.add(node)
            t = max(t,w)
            for n1,w1 in edges[node]:
                if n1 not in visit:
                    heapq.heappush(minHeap,(w1+w,n1))
        return t if len(visit) == n else -1



