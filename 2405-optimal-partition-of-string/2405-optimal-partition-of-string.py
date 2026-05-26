class Solution:
    def partitionString(self, s: str) -> int:
        curset= set()
        res = 1
        for c in s:
            if c in curset:
                res+=1
                curset = set()
                curset.add(c)
            curset.add(c)
        return res