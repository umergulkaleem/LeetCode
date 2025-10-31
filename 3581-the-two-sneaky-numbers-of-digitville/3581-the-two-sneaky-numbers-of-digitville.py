class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        final  = []
        for i,v in freq.items():
            if v == 2:
                final.append(i)
        return final
        