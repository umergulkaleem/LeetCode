class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0

        for i in range(len(s)):
            
            point1 = i
            point2 = i
        

            while point1>=0 and point2<len(s) and s[point1] == s[point2]:
                    point1-=1
                    point2+=1

            length = point2-point1-1
            point1 = i
            point2 = i+1
            length1 = 0
            while point1>=0 and point2<len(s) and s[point1] == s[point2]:
                    point1-=1
                    point2+=1
                    length1+=1
            length1  = point2-point1 -1

            maxlen = max(length,length1)

            if maxlen > (end-start):
                start = i - (maxlen - 1) // 2
                end   = i + maxlen // 2

        return s[start:end+1]

            
                    

        