class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # pattern= []
        # count = 0
        # curr = ""
        # for i in range(len(s)):
        #     if count>numRows+1:
        #         pattern.append([curr])
        #         count=0
        #     if i % numRows == 0:
        #         pattern.append([curr])
        #         curr=""
        #     curr+=s[i]
        #     count+=1
        #     print(count,"coint")
        # print(pattern)
        
        if numRows == 1:
            return s
        res = ""

        for r in range(numRows):
            increments = 2 *(numRows-1)
            for i in range(r,len(s),increments):
                
                res+=s[i]
                if (r>0 and r<numRows-1 and
                i+increments -2 * r<len(s)):
                    res+=s[i+increments -2 * r]
        return res
