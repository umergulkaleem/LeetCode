class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        openb = 0
        res = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
                openb+=1
                res = max(res,openb)
            elif ch == ")":
                stack.pop()
                openb-=1
            else:
                continue
        return res


        