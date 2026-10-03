class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs = {}
        stack = []

        for i,c in enumerate(s):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                j = stack.pop()
                pairs[i]=j
                pairs[j]=i
            # print(pairs)
        res = []
        i,direction = 0,1

        while i<len(s):
            if s[i] == "(" or s[i] == ")":
                # print(pairs[i])
                i = pairs[i]
                direction = -direction
            else:
                res.append(s[i])
        
            i+=direction
        
        return "".join(res)  

        