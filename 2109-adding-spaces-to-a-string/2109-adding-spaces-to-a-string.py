class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # p1 = 0
        # p2 = 0
        # res = []
        # while p2 < len(spaces) orp1 < len(s):
        #     if p1== spaces[p2]:
        #         res.append(" ")
        #         p2+=1
        #     res.append(s[p1])
        #     p1+=1
        # return "".join(res)
        p1 =0 
        p2 = 0
        res = []
        for p1 in range(len(s)):
            if p2<len(spaces) and p1==spaces[p2]:
                res.append(" ")
                p2+=1
            res.append(s[p1])
        return "".join(res)


        