class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        string = ""
        l = 0
        length = float("inf")
        ones = 0
        for r in range(len(s)):
            # tmp+=s[r]
            if s[r] == "1":
                ones+=1
            
            while ones>k:
                if s[l] == "1":
                    ones-=1   
                l+=1
            if ones ==k:
                while s[l] == "0":
                    l+=1
                if  length>r-l+1:

                    length= r-l+1
                    string = s[l:r+1]

                elif length == r-l+1 and string>s[l:r+1]:
                    length= r-l+1
                    string = s[l:r+1]
            
        return string
