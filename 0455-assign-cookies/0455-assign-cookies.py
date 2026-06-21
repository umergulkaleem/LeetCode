class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        p1 = 0
        p2 = 0
        res  = 0
        if len(s) == 0 or len(g) == 0:
            return 0
        g  = sorted(g)
        s = sorted(s)
        while p1<len(g) and p2 < len(s):
            print(p1,p2)
            if g[p1]<=s[p2]:
                p1+=1
                res+=1
            p2+=1
        return res


        