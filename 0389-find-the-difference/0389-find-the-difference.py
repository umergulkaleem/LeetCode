class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        print(count_s)
        print(count_t)
        dict1 = count_t-count_s
        return list(dict1.keys())[0]
        

        