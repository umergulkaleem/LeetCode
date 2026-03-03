class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj = {src:[] for src,des in tickets}
        # tickets.sort()
        # for src, des in tickets:
        #     adj[src].append(des)

        # res = ["JFK"]

        # def dfs(src):
        #     if len(res) == len(tickets)+1:
        #         return True
        #     if src not in adj:
        #         return False
        #     for i in range(len(adj[src])):
        #         v = adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v):return True
        #         adj[src].insert(i,v)
        #         res.pop()
        #     return False
        # dfs("JFK")
        # return res
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        # Sort EACH airport's destinations for lex smallest
        for src in adj:
            adj[src].sort()
        
        res = []
        def dfs(curr):
            while adj[curr]:
                next = adj[curr].pop(0)  # Take SMALLEST first
                dfs(next)
            res.append(curr)
        
        dfs("JFK")
        return res[::-1]