class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def sub(s,subseq):
            p1,p2 = 0,0
            while p1<len(s) and p2<len(subseq):
                if p1 in removed :
                    p1+=1
                    continue
                if s[p1] == subseq[p2]:
                    p2+=1
                p1+=1
            return p2 == len(subseq)
        
        l,r = 0,len(removable)
        res = 0
        while l<=r:
            m = (l+r)//2
            removed = set(removable[:m])
            if sub(s,p):
                res = max(res,m)
                l = m+1
            else:
                r = m - 1
        return res