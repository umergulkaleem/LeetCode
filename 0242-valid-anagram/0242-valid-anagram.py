class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!= len(t):
        #     return False
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        count_s = Counter(s)
        count_t = Counter(t)
        return True if count_s==count_t else False
        