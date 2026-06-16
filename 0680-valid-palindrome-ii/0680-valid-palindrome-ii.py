class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        p1,p2 = 0,len(s)-1
        def helper(p1,p2):
            while p1<p2:
                if s[p1]!=s[p2]:
                    return False
                p1+=1
                p2-=1
            return True
        
        while p1<p2:
            if s[p1]!=s[p2]:
                return helper(p1+1,p2) or helper(p1,p2-1)

            p1+=1
            p2-=1
        return True


        