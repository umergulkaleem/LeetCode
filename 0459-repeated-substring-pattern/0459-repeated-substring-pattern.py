class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # counters =Counter(s)
        # if len(s) == 1 or len(s) == 0:
        #     return False
        # if  len(set(counters.values())) == 1:
        #     return True
        # else:
        #     return False
        modified = (s+s)[1:-1]

        return s in modified