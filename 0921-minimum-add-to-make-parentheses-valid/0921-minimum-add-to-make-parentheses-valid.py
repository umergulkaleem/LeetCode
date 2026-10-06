class Solution:
    def minAddToMakeValid(self, s: str) -> int:


        # stack = []

        # prev = s[0]

        # for i in range(1,len(s)):
        #     curr = s[i]
        #     print("at",prev,curr)
        #     if prev == "("  and curr == ")":
        #         print("in")
        #         continue
        #     else:
        #         stack.append(curr)
        #     prev = curr
        # return len(stack)

        count = 0
        res =0 

        for i in s:
            if i  == "(":
                count+=1
            else:
                if count == 0:
                    res+=1
                count  =max(count-1,0)
        return res+count



        