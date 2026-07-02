class Solution:
    def maxScore(self, s: str) -> int:
        right_one  = s.count("1")
        zero = 0
        ans = 0

        for i in range(len(s)-1):
            if s[i] == "0":
                zero+=1
            else:
                right_one -=1
            
            ans = max(ans,right_one+zero)
        return ans
        