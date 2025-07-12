class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        last = s[len(s)-1]
        return len(last)