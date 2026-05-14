class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seen , res = set(),set()

        for i in range(len(s)-9):
            curr = s[i:i+10]

            if curr in seen:
                res.add(curr)
            else:
                seen.add(curr)
        return list(res)
        