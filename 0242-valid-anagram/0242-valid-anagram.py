class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1,count2 = {},{}
        for i in range(len(s)):
            count1[s[i]] = 1+count1.get(s[i],0)
            count2[t[i]] = 1+count2.get(t[i],0)

        for c in count1:
            if count1[c]!=count2.get(c,0):
                return False
        return True

        