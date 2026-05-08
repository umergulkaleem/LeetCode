class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        prev = ord(s[0])
        for i in range(1,len(s)):
            print(prev,"prev")
            curr = ord(s[i])
            print(curr,"current")
            res+= abs(prev - curr)
            prev = curr
        return res


        